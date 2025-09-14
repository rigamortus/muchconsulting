from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert data["status"] == "ok"
    assert "message" in data

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["health"] == "pass"

def test_info():
    response = client.get("/info")
    assert response.status_code == 200
    data = response.json()
    assert "app" in data
    assert "version" in data

def test_metrics():
    response = client.get("/metrics")
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/plain")
    assert b"app_cpu_percent" in response.content
    assert b"app_memory_percent" in response.content