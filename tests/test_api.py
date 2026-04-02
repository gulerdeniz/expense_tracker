from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Expense Tracker API is Running"}

def test_create():
    payload = {
        "amount": 100,
        "category": "food",
        "description": "dinner",
        "date": "2026-03-17"
    }
    response = client.post("/expenses", json=payload)
    data = response.json()

    assert response.status_code == 200
    assert data["amount"] == 100
    assert data["category"] == "food"
    assert data["description"] == "dinner"
    assert data["date"] == "2026-03-17"

    assert id in data

def test_get_expenses():
    payload1 = {
        "amount": 100,
        "category": "food",
        "description": "dinner",
        "date": "2026-03-17"
    }

    payload2 = {
        "amount": 200,
        "category": "food",
        "description": "dinner",
        "date": "2026-04-14"
    }
    client.post("/expenses", json=payload1)
    client.post("/expenses", json=payload2)

    response = client.get("/expenses")

    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) >=2

def test_get_expenses_by_id():
    payload = {
        "amount": 100,
        "category": "food",
        "description": "dinner",
        "date": "2026-03-17"
    }
    post_response = client.post("/expenses",json=payload)

    post_data = post_response.json()

    expense_id = post_data["id"]

    get_response = client.get(f"/expenses/{expense_id}")

    get_data = get_response.json()

    assert get_response.status_code == 200
    assert get_data["amount"] == 100
    assert get_data["category"] == "food"
    assert get_data["description"] == "dinner"
    assert get_data["date"] == "2026-03-17"

def test_delete_expenses():
    payload = {
        "amount": 100,
        "category": "food",
        "description": "dinner",
        "date": "2026-03-17"
    }

    post_response = client.post("/expenses", json=payload)

    data_post = post_response.json()

    expense_id = data_post["id"]

    delete_response = client.delete(f"/expenses/{expense_id}")

    assert delete_response.status_code == 200

    get_response = client.get(f"/expenses/{expense_id}")

    assert get_response.status_code == 404

def test_put_expenses():
    payload1 = {
        "amount": 100,
        "category": "food",
        "description": "dinner",
        "date": "2026-03-17"
    }

    payload2 = {
        "amount": 200,
        "category": "food",
        "description": "dinner",
        "date": "2026-04-14"
    }

    post_response = client.post("/expenses", json=payload1)

    post_data = post_response.json()

    expense_id = post_data["id"]

    put_response = client.put(f"/expenses/{expense_id}", json= payload2)

    assert put_response.status_code == 200

    get_response = client.get(f"/expenses/{expense_id}")

    assert get_response.status_code == 200

    get_data = get_response.json()

    assert get_data["id"] == expense_id
    assert get_data["amount"] == payload2["amount"]
    assert get_data["category"] == payload2["category"]
    assert get_data["description"] == payload2["description"]
    assert get_data["date"] == payload2["date"]