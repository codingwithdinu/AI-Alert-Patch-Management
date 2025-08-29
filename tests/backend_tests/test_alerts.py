from fastapi.testclient import TestClient
from backend.app.main import app
client = TestClient(app)

def test_create_alert_and_list():
    r = client.post("/alerts/", json={"source":"monitor","message":"CPU 95% on node"})
    assert r.status_code == 200
    a = r.json()
    assert a["priority"] in {"critical","high","medium","low"}

    r2 = client.get("/alerts/")
    assert r2.status_code == 200
    assert len(r2.json()) >= 1
