from typing import Annotated

from fastapi import Depends
from models import User
from routers import USER_AUTHORIZATION_EXCEPTION, INCORRECT_PASSWORD_EXCEPTION
from routers.auth import BCRYPT_CONTEXT
from routers.auth.auth_user_validation import UserValidation
from routers.helpers import get_db
from routers.user.user_models import ChangePasswordRequest
from sqlalchemy.orm import Session

DB_DEPENDENCY = Annotated[Session, Depends(get_db)]
USER_DEPENDENCY = Annotated[dict, Depends(UserValidation.get_current_user)]


async def get_account_details(user: USER_DEPENDENCY, db: DB_DEPENDENCY) -> list[User]:
    if not user:
        raise USER_AUTHORIZATION_EXCEPTION
    return db.query(User).filter(User.id == user.get("user_id")).first()


async def change_password(
    user: USER_DEPENDENCY,
    db: DB_DEPENDENCY,
    password_verification: ChangePasswordRequest,
):
    if not user:
        raise USER_AUTHORIZATION_EXCEPTION
    users_table = db.query(User).filter(User.id == user.get("user_id")).first()
    if not BCRYPT_CONTEXT.verify(
        password_verification.current_password, users_table.hashed_password
    ):
        raise INCORRECT_PASSWORD_EXCEPTION
    users_table.hashed_password = BCRYPT_CONTEXT.hash(
        password_verification.new_password
    )
    db.add(users_table)
    db.commit()
