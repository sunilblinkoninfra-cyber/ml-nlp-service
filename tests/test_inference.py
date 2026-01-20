import requests

BASE = "http://localhost:8001"

def test_benign():
    r = requests.post(f"{BASE}/analyze/text", json={
        "subject": "Team meeting notes",
        "body": "Please find the notes attached."
    })
    assert r.status_code == 200
    assert r.json()["text_ml_score"] < 0.5

def test_phishing():
    r = requests.post(f"{BASE}/analyze/text", json={
        "subject": "Urgent: Account Suspended",
        "body": "Verify your account immediately to avoid suspension."
    })
    assert r.status_code == 200
    assert r.json()["text_ml_score"] > 0.6
