import joblib
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Minimal starter dataset (replace later with real corpora)
texts = [
    "team meeting notes attached",
    "invoice for last month",
    "please review the document",
    "urgent verify your account immediately",
    "your account is suspended click to verify",
    "password reset required immediately",
]
labels = [0, 0, 0, 1, 1, 1]

pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(
        ngram_range=(1, 2),
        analyzer="word",
        min_df=1,
        max_features=20000
    )),
    ("clf", LogisticRegression(
        max_iter=1000,
        class_weight="balanced"
    ))
])

pipeline.fit(texts, labels)

joblib.dump(pipeline, "models/tfidf_lr.joblib")
print("Model saved to models/tfidf_lr.joblib")
