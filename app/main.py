from fastapi import FastAPI
from app.schema import TextAnalysisRequest
from services.nlp_model import predict
from services.explainability import explain

app = FastAPI(title="NLP Phishing Detection Service (Lightweight)")

@app.post("/analyze/text")
def analyze_text(payload: TextAnalysisRequest):
    score = predict(payload.subject, payload.body)
    reasons = explain(score, payload.subject, payload.body)

    return {
        "text_ml_score": round(score, 2),
        "signals": reasons,
        "model_version": "nlp-tfidf-v1.0.0"
    }
