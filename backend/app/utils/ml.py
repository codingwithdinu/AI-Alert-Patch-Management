# Loads a trained model if present; otherwise uses a simple rules fallback.
from pathlib import Path
from joblib import load

MODEL_PATH = Path(__file__).resolve().parents[2] / "ml" / "models" / "alert_classifier.joblib"

keywords = {
    "critical": ["outage", "down", "breach", "ransom", "panic", "database down"],
    "high": ["failed", "error", "high cpu", "disk full", "unauthorized"],
    "medium": ["warning", "retry", "latency", "delay"],
    "low": ["info", "notice", "debug"]
}

_pipeline = None
if MODEL_PATH.exists():
    try:
        _pipeline = load(MODEL_PATH)
    except Exception:
        _pipeline = None

def predict_priority(text: str) -> str:
    global _pipeline
    if _pipeline:
        label = _pipeline.predict([text])[0]
        return str(label)
    t = text.lower()
    for p, words in keywords.items():
        if any(w in t for w in words):
            return p
    return "low"
