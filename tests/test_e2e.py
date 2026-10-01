from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "OK", "message": "Application is healthy"}

def test_data_endpoint():
    response = client.get("/api/data")
    assert response.status_code == 200
    assert "item1" in response.json()["data"]