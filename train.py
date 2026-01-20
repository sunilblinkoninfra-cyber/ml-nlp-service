import joblib
import numpy as np
import torch
from transformers import DistilBertTokenizer, DistilBertModel
from sklearn.linear_model import LogisticRegression

# ---- Minimal toy training data (replace with real datasets) ----
X = [
    "Team meeting notes attached",
    "Invoice for last month",
    "Urgent verify your account immediately",
    "Your account is suspended click to verify"
]
y = [0, 0, 1, 1]

tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")
bert = DistilBertModel.from_pretrained("distilbert-base-uncased")
bert.eval()

def embed(texts):
    embs = []
    for t in texts:
        inputs = tokenizer(t, truncation=True, padding=True, max_length=256, return_tensors="pt")
        with torch.no_grad():
            out = bert(**inputs)
        embs.append(out.last_hidden_state.mean(dim=1).numpy()[0])
    return np.vstack(embs)

X_emb = embed(X)

clf = LogisticRegression(max_iter=1000)
clf.fit(X_emb, y)

joblib.dump(clf, "models/distilbert_lr.joblib")
print("Model saved to models/distilbert_lr.joblib")
