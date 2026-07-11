from datetime import timedelta
from typing import Annotated

from fastapi import Request, Depends
from fastapi.security import OAuth2PasswordRequestForm

from .models import CreateUserRequest, Token
from .. import DB_DEPENDENCY
from ..config import BCRYPT_CONTEXT
from ..exceptions import USER_CREATION_EXCEPTION, USER_AUTHENTICATION_EXCEPTION
from ..user_validation import HandleUser
from ... import TEMPLATES
from ...models import User


# Pages
def render_login_page_handler(request: Request):
    return TEMPLATES.TemplateResponse("login.html", {"request": request})


def render_register_page_handler(request: Request):
    return TEMPLATES.TemplateResponse("register.html", {"request": request})


# Endpoints
async def create_user_handler(
    db: DB_DEPENDENCY, create_user_request: CreateUserRequest
):
    role = create_user_request.role.lower().strip()
    if role not in ["admin", "user"]:
        raise USER_CREATION_EXCEPTION
    row = User(
        email=str(create_user_request.email).lower().strip(),
        username=create_user_request.username.strip(),
        first_name=create_user_request.first_name.title().strip(),
        last_name=create_user_request.last_name.title().strip(),
        hashed_password=BCRYPT_CONTEXT.hash(create_user_request.password.strip()),
        role=role,
        phone_number=create_user_request.phone_number.strip(),
    )
    db.add(row)
    db.commit()


# Creates and returns the JWT after authenticating the user login
async def create_token_handler(
    db: DB_DEPENDENCY, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> dict[str, Token | str]:
    user = HandleUser.authenticate_user_login(
        form_data.username, form_data.password, db
    )
    if not user:
        raise USER_AUTHENTICATION_EXCEPTION
    token = HandleUser.create_access_token(
        user.username, user.id, user.role, timedelta(minutes=20)
    )
    return {"access_token": token, "token_type": "bearer"}
