"""
Trains a tiny text classifier to map alert messages -> priority.
Saves to ml/models/alert_classifier.joblib
"""
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from joblib import dump
from pathlib import Path

data = [
    ("Database down for prod cluster", "critical"),
    ("Ransomware detected on server", "critical"),
    ("CPU 95% on api-node-3", "high"),
    ("Disk utilization 92% on /var", "high"),
    ("Login failed attempts spike", "high"),
    ("Latency increased on checkout", "medium"),
    ("Warning: TLS cert expiring soon", "medium"),
    ("Info: nightly backup completed", "low"),
    ("Debug: verbose logging enabled", "low"),
]

X, y = zip(*data)

pipeline = make_pipeline(
    TfidfVectorizer(ngram_range=(1,2), min_df=1),
    LogisticRegression(max_iter=500)
)
pipeline.fit(X, y)

out = Path(__file__).resolve().parent / "models" / "alert_classifier.joblib"
out.parent.mkdir(parents=True, exist_ok=True)
dump(pipeline, out)
print(f"Saved model to {out}")
