from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_valid_domain():
    response = client.get("/check?target=kaushalkhatiwada.com.np")
    assert response.status_code == 200

def test_fake_domain():
    response = client.get("/check?target=kk.com")
    assert response.status_code == 200 or response.status_code == 404 or response.status_code == 503

def test_invalid_domain():
    response = client.get("/check?target=fuse machinecom")
    assert response.status_code == 400
