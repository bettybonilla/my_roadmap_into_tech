from .user_models import ChangePasswordRequest, ChangePhoneNumberRequest
from .. import (
    USER_DEPENDENCY,
    DB_DEPENDENCY,
    USER_AUTHORIZATION_EXCEPTION,
    INCORRECT_PASSWORD_EXCEPTION,
)
from ..auth import BCRYPT_CONTEXT
from ...models import User


async def get_account_details_handler(
    user: USER_DEPENDENCY, db: DB_DEPENDENCY
) -> list[User]:
    if not user:
        raise USER_AUTHORIZATION_EXCEPTION
    return db.query(User).filter(User.id == user.get("user_id")).first()


async def change_password_handler(
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


async def change_phone_number_handler(
    user: USER_DEPENDENCY,
    db: DB_DEPENDENCY,
    change_phone_number_request: ChangePhoneNumberRequest,
):
    if not user:
        raise USER_AUTHORIZATION_EXCEPTION
    users_table = db.query(User).filter(User.id == user.get("user_id")).first()
    users_table.phone_number = change_phone_number_request.new_phone_number
    db.add(users_table)
    db.commit()
