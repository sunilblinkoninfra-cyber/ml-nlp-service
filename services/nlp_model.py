import joblib
import torch
import numpy as np
from transformers import DistilBertTokenizer, DistilBertModel

MODEL_PATH = "models/distilbert_lr.joblib"

tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")
bert = DistilBertModel.from_pretrained("distilbert-base-uncased")
bert.eval()  # inference only

classifier = joblib.load(MODEL_PATH)

def _embed(text: str) -> np.ndarray:
    inputs = tokenizer(
        text,
        truncation=True,
        padding=True,
        max_length=256,
        return_tensors="pt"
    )
    with torch.no_grad():
        outputs = bert(**inputs)
    # Mean pooling
    return outputs.last_hidden_state.mean(dim=1).cpu().numpy()

def predict(subject: str, body: str) -> float:
    text = f"{subject} {body}".strip()
    vec = _embed(text)
    prob = classifier.predict_proba(vec)[0][1]
    return float(prob)
