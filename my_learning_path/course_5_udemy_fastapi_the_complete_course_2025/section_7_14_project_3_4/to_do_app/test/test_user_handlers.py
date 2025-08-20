from fastapi import status

from . import client
from .helpers import mock_get_db, mock_get_current_user, mock_users_table
from ..main import app
from ..routers.auth.auth_user_validation import UserValidation
from ..routers.helpers import get_db

app.dependency_overrides[get_db] = mock_get_db
app.dependency_overrides[UserValidation.get_current_user] = mock_get_current_user


def test_get_account_details_handler(mock_users_table):
    response = client.get("user/account-details")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["email"] == "codingwithroby@email.com"
    assert response.json()["username"] == "codingwithroby"
    assert response.json()["first_name"] == "Eric"
    assert response.json()["last_name"] == "Roby"
    assert response.json()["role"] == "admin"
    assert response.json()["phone_number"] == "111-111-1111"


def test_change_password_handler(mock_users_table):
    response = client.put(
        "user/change-password",
        json={"current_password": "testpassword", "new_password": "newpassword"},
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_change_password_handler_unauthorized(mock_users_table):
    response = client.put(
        "user/change-password",
        json={"current_password": "incorrect password", "new_password": "newpassword"},
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {"detail": "Incorrect password"}


def test_change_phone_number_handler(mock_users_table):
    response = client.put(
        "user/change-phone-number",
        json={"new_phone_number": "222-222-2222"},
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT
