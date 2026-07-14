from app import app

def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}

def test_add_and_get_task():
    client = app.test_client()
    response = client.post("/tasks", json={"title": "Write tests"})
    assert response.status_code == 201
    assert response.get_json()["title"] == "Write tests"

    response = client.get("/tasks")
    assert response.status_code == 200
    titles = [t["title"] for t in response.get_json()]
    assert "Write tests" in titles