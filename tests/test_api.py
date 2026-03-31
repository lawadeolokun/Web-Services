from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_all():
    response = client.get("/getAll")
    assert response.status_code == 200

def test_add_product():
    data = {
        "ProductID": 999,
        "Name": "Test",
        "UnitPrice": 10.0,
        "StockQuantity": 5,
        "Description": "Test item"
    }
    response = client.post("/addNew", json=data)
    assert response.status_code == 200