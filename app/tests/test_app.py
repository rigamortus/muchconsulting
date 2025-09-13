from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["health"] == "pass"

def test_info():
    response = client.get("/info")
    assert response.status_code == 200
    assert "app" in response.json()
    assert "version" in response.json()