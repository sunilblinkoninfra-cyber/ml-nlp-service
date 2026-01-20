import joblib

MODEL_PATH = "models/tfidf_lr.joblib"

model = joblib.load(MODEL_PATH)

def predict(subject: str, body: str) -> float:
    text = f"{subject} {body}".strip()
    prob = model.predict_proba([text])[0][1]
    return float(prob)
