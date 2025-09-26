from fastapi import status

from . import client, TestSessionLocal
from .helpers import mock_get_db, mock_get_current_user, mock_to_do
from ..main import app
from ..models import ToDo
from ..routers.helpers import get_db
from ..routers.user_validation import HandleUser

app.dependency_overrides[get_db] = mock_get_db
app.dependency_overrides[HandleUser.get_current_user] = mock_get_current_user


def test_read_all_to_dos_handler(mock_to_do):
    response = client.get("/to-dos")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [
        {
            "id": 1,
            "title": "Learn to code!",
            "description": "Need to learn everyday!",
            "priority": 5,
            "complete": False,
            "owner_id": 1,
        }
    ]


def test_read_to_do_handler(mock_to_do):
    response = client.get("/to-dos/1")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "id": 1,
        "title": "Learn to code!",
        "description": "Need to learn everyday!",
        "priority": 5,
        "complete": False,
        "owner_id": 1,
    }


def test_read_to_do_handler_not_found():
    response = client.get("/to-dos/999")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "To-do not found"}


def test_create_to_do_handler(mock_to_do):
    to_do_request = {
        "title": "New to-do",
        "description": "New to-do description",
        "priority": 5,
        "complete": False,
    }
    response = client.post("/to-dos/create-to-do", json=to_do_request)
    assert response.status_code == status.HTTP_201_CREATED
    db = TestSessionLocal()
    row = db.query(ToDo).filter(ToDo.id == 2).first()
    assert row.title == to_do_request.get("title")
    assert row.description == to_do_request.get("description")
    assert row.priority == to_do_request.get("priority")
    assert row.complete == to_do_request.get("complete")


def test_update_to_do_handler(mock_to_do):
    to_do_request = {
        "title": "Change the title of the to-do already saved!",
        "description": "Need to learn everyday!",
        "priority": 5,
        "complete": False,
    }
    response = client.put("/to-dos/update-to-do/1", json=to_do_request)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    db = TestSessionLocal()
    row = db.query(ToDo).filter(ToDo.id == 1).first()
    assert row.title == to_do_request.get("title")
    assert row.description == to_do_request.get("description")
    assert row.priority == to_do_request.get("priority")
    assert row.complete == to_do_request.get("complete")


def test_update_to_do_handler_not_found(mock_to_do):
    to_do_request = {
        "title": "Change the title of the to-do already saved!",
        "description": "Need to learn everyday!",
        "priority": 5,
        "complete": False,
    }
    response = client.put("/to-dos/update-to-do/999", json=to_do_request)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "To-do not found"}


def test_delete_to_do_handler(mock_to_do):
    response = client.delete("/to-dos/delete-to-do/1")
    assert response.status_code == status.HTTP_204_NO_CONTENT
    db = TestSessionLocal()
    row = db.query(ToDo).filter(ToDo.id == 1).first()
    assert row is None


def test_delete_to_do_handler_not_found():
    response = client.delete("/to-dos/delete-to-do/999")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "To-do not found"}
