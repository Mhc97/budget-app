from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    
    
def test_create_expense():
    response = client.post("/expenses", json={
        "title":"Test",
        "amount": 10.0,
        "category": "Test"
    })
    
    assert response.status_code == 200
    assert response.json()["title"] == "Test"
    
def test_get_expenses():
    response = client.get("/expenses")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    
