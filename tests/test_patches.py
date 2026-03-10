import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine

@pytest.fixture(autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

client = TestClient(app)

def test_health_check():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_create_and_list_patch():
    payload = {
        "patch_id": "TEST-001",
        "title": "Test Patch",
        "severity": "high",
    }
    r = client.post("/api/v1/patches/", json=payload)
    assert r.status_code == 201
    data = r.json()
    assert data["patch_id"] == "TEST-001"
    assert data["risk_score"] > 0

    r2 = client.get("/api/v1/patches/")
    assert r2.status_code == 200
    assert len(r2.json()) == 1

def test_duplicate_patch_id():
    payload = {"patch_id": "DUP-001", "title": "Dup", "severity": "low"}
    client.post("/api/v1/patches/", json=payload)
    r = client.post("/api/v1/patches/", json=payload)
    assert r.status_code == 400

def test_delete_patch():
    payload = {"patch_id": "DEL-001", "title": "Delete Me", "severity": "medium"}
    r = client.post("/api/v1/patches/", json=payload)
    pid = r.json()["id"]
    r2 = client.delete(f"/api/v1/patches/{pid}")
    assert r2.status_code == 204

def test_create_alert_rule():
    payload = {"name": "Test Rule", "severity_filter": "critical", "min_risk_score": 50.0}
    r = client.post("/api/v1/alert-rules/", json=payload)
    assert r.status_code == 201
    assert r.json()["name"] == "Test Rule"