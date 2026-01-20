PHRASE_SIGNALS = [
    ("urgent", "Urgency language"),
    ("verify", "Account verification request"),
    ("suspended", "Threat of suspension"),
    ("click", "Call-to-action link"),
    ("password", "Credential request"),
    ("immediately", "Time pressure"),
]

def explain(score: float, subject: str, body: str):
    reasons = []
    text = f"{subject} {body}".lower()

    for phrase, label in PHRASE_SIGNALS:
        if phrase in text:
            reasons.append(label)

    if score >= 0.8:
        reasons.append("High phishing intent detected")
    elif score >= 0.6:
        reasons.append("Moderate phishing intent detected")

    # De-duplicate while preserving order
    seen = set()
    out = []
    for r in reasons:
        if r not in seen:
            seen.add(r)
            out.append(r)
    return out
