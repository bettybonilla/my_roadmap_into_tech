from datetime import timedelta, datetime, timezone

import pytest
from fastapi import HTTPException
from jose import jwt

from . import TestSessionLocal
from .helpers import mock_get_db, mock_user
from ..main import app
from ..routers.config import SECRET, ALGORITHM
from ..routers.helpers import get_db
from ..routers.user_validation import HandleUser

app.dependency_overrides[get_db] = mock_get_db


def test_authenticate_user_login(mock_user):
    db = TestSessionLocal()
    user = HandleUser.authenticate_user_login(mock_user.username, "testpassword", db)
    assert user is not None
    assert user.username == mock_user.username
    false_username = HandleUser.authenticate_user_login(
        "incorrect username", "testpassword", db
    )
    assert false_username is False
    false_password = HandleUser.authenticate_user_login(
        mock_user.username, "incorrect password", db
    )
    assert false_password is False


def test_create_access_token():
    username = "testusername"
    user_id = 1
    user_role = "user"
    expires_delta = timedelta(days=1)
    encoded_jwt = HandleUser.create_access_token(
        username, user_id, user_role, expires_delta
    )
    decoded_jwt = jwt.decode(
        encoded_jwt,
        key=SECRET,
        algorithms=ALGORITHM,
        options={"verify_signature": False},
    )
    assert decoded_jwt["sub"] == username
    assert decoded_jwt["id"] == user_id
    assert decoded_jwt["role"] == user_role


@pytest.mark.asyncio
async def test_get_current_user():
    payload = {
        "sub": "testusername",
        "id": 1,
        "role": "admin",
        "exp": datetime.now(timezone.utc) + timedelta(days=1),
    }
    encoded_jwt = jwt.encode(algorithm=ALGORITHM, claims=payload, key=SECRET)
    user = await HandleUser.get_current_user(token=encoded_jwt)
    assert user == {"username": "testusername", "user_id": 1, "user_role": "admin"}


@pytest.mark.asyncio
async def test_get_current_user_unauthorized():
    payload = {"sub": "testusername"}
    encoded_jwt = jwt.encode(algorithm=ALGORITHM, claims=payload, key=SECRET)

    with pytest.raises(HTTPException) as excinfo:
        await HandleUser.get_current_user(token=encoded_jwt)

    assert excinfo.value.status_code == 401
    assert excinfo.value.detail == "Authentication failed"
