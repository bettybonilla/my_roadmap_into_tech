from .models import ChangePasswordRequest, ChangePhoneNumberRequest
from .. import USER_DEPENDENCY, DB_DEPENDENCY
from ..config import BCRYPT_CONTEXT
from ..exceptions import USER_AUTHORIZATION_EXCEPTION, INCORRECT_PASSWORD_EXCEPTION
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
    row = db.query(User).filter(User.id == user.get("user_id")).first()
    if not BCRYPT_CONTEXT.verify(
        password_verification.current_password, row.hashed_password
    ):
        raise INCORRECT_PASSWORD_EXCEPTION
    row.hashed_password = BCRYPT_CONTEXT.hash(password_verification.new_password)
    db.add(row)
    db.commit()


async def change_phone_number_handler(
    user: USER_DEPENDENCY,
    db: DB_DEPENDENCY,
    change_phone_number_request: ChangePhoneNumberRequest,
):
    if not user:
        raise USER_AUTHORIZATION_EXCEPTION
    row = db.query(User).filter(User.id == user.get("user_id")).first()
    row.phone_number = change_phone_number_request.new_phone_number
    db.add(row)
    db.commit()
