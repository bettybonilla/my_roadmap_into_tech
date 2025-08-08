from datetime import timedelta
from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from models import User
from routers import USER_AUTHENTICATION_EXCEPTION
from routers.auth import BCRYPT_CONTEXT
from routers.auth.auth_models import (
    CreateUserRequest,
    Token,
)
from routers.auth.auth_user_validation import UserValidation
from routers.helpers import get_db
from sqlalchemy.orm import Session

DB_DEPENDENCY = Annotated[Session, Depends(get_db)]


async def create_user_handler(
    db: DB_DEPENDENCY, create_user_request: CreateUserRequest
):
    users_table = User(
        email=create_user_request.email,
        username=create_user_request.username,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        hashed_password=BCRYPT_CONTEXT.hash(create_user_request.password),
        role=create_user_request.role,
        phone_number=create_user_request.phone_number,
    )
    db.add(users_table)
    db.commit()


# Creates and returns the JWT after authenticating the user login
async def create_token_handler(
    db: DB_DEPENDENCY, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> dict[str, Token | str]:
    user = UserValidation.authenticate_user_login(
        form_data.username, form_data.password, db
    )
    if not user:
        raise USER_AUTHENTICATION_EXCEPTION
    token = UserValidation.get_access_token(
        user.username, user.id, user.role, timedelta(minutes=20)
    )
    return {"access_token": token, "token_type": "bearer"}
