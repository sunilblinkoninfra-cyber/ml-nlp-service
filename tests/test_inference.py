import requests

BASE = "http://localhost:8001"

def test_benign():
    r = requests.post(f"{BASE}/analyze/text", json={
        "subject": "Team meeting notes",
        "body": "Please see attached."
    })
    assert r.status_code == 200
    assert r.json()["text_ml_score"] < 0.5

def test_phishing():
    r = requests.post(f"{BASE}/analyze/text", json={
        "subject": "Urgent account suspension",
        "body": "Verify immediately to avoid suspension."
    })
    assert r.status_code == 200
    assert r.json()["text_ml_score"] > 0.6
