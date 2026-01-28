from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_todo():
    response = client.post("/todos", json={"title": "Test Todo"})
    assert response.status_code == 201
    assert response.json()["title"] == "Test Todo"


def test_get_todos():
    response = client.get("/todos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_update_todo():
    create = client.post("/todos", json={"title": "Old Title"})
    todo_id = create.json()["id"]

    update = client.put(f"/todos/{todo_id}", json={"title": "New Title"})
    assert update.status_code == 200
    assert update.json()["title"] == "New Title"


def test_delete_todo():
    create = client.post("/todos", json={"title": "Delete Me"})
    todo_id = create.json()["id"]

    delete = client.delete(f"/todos/{todo_id}")
    assert delete.status_code == 204
