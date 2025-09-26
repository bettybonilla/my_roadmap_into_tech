from typing import NoReturn

from fastapi import Path

from .. import USER_DEPENDENCY, DB_DEPENDENCY
from ..exceptions import (
    USER_AUTHORIZATION_EXCEPTION,
    USER_FORBIDDEN_EXCEPTION,
    TO_DO_NOT_FOUND_EXCEPTION,
)
from ...models import ToDo


class AdminAccess:
    @staticmethod
    async def read_all_to_dos_handler(
        user: USER_DEPENDENCY,
        db: DB_DEPENDENCY,
    ) -> list[ToDo | NoReturn]:
        if not user:
            raise USER_AUTHORIZATION_EXCEPTION
        if user.get("user_role") != "admin":
            raise USER_FORBIDDEN_EXCEPTION
        # Returns all the to-dos we currently have in this database table
        return db.query(ToDo).all()

    @staticmethod
    async def delete_to_do_handler(
        user: USER_DEPENDENCY, db: DB_DEPENDENCY, to_do_id: int = Path(gt=0)
    ):
        if not user:
            raise USER_AUTHORIZATION_EXCEPTION
        if user.get("user_role") != "admin":
            raise USER_FORBIDDEN_EXCEPTION
        row = db.query(ToDo).filter(ToDo.id == to_do_id).first()
        if not row:
            raise TO_DO_NOT_FOUND_EXCEPTION
        db.query(ToDo).filter(ToDo.id == to_do_id).delete()
        db.commit()
