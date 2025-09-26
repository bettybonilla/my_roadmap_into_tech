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
    response = client.get("admin/to-dos")
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


def test_delete_to_do_handler(mock_to_do):
    response = client.delete("admin/to-dos/delete-to-do/1")
    assert response.status_code == status.HTTP_204_NO_CONTENT
    db = TestSessionLocal()
    row = db.query(ToDo).filter(ToDo.id == 1).first()
    assert row is None


def test_delete_to_do_handler_not_found():
    response = client.delete("admin/to-dos/delete-to-do/999")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "To-do not found"}
