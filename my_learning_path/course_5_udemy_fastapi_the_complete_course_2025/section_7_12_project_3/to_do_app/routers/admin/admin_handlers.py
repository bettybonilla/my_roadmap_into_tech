from typing import Annotated, NoReturn

from fastapi import Depends, Path
from models import ToDo
from routers import USER_AUTHORIZATION_EXCEPTION
from routers.auth.auth_user_validation import UserValidation
from routers.helpers import get_db
from sqlalchemy.orm import Session

DB_DEPENDENCY = Annotated[Session, Depends(get_db)]
USER_DEPENDENCY = Annotated[dict, Depends(UserValidation.get_current_user)]


class AdminAccess:
    @staticmethod
    async def read_all_to_dos_handler(
        user: USER_DEPENDENCY,
        db: DB_DEPENDENCY,
    ) -> list[ToDo | NoReturn]:
        if not user or user.get("user_role") != "admin":
            raise USER_AUTHORIZATION_EXCEPTION
        # Returns all the to-dos we currently have in this database table
        return db.query(ToDo).all()

    @staticmethod
    async def delete_to_do_handler(
        user: USER_DEPENDENCY, db: DB_DEPENDENCY, to_do_id: int = Path(gt=0)
    ):
        if not user or user.get("user_role") != "admin":
            raise USER_AUTHORIZATION_EXCEPTION
        to_dos_table = db.query(ToDo).filter(ToDo.id == to_do_id).first()
        if not to_dos_table:
            raise TO_DO_NOT_FOUND_EXCEPTION
        db.query(ToDo).filter(ToDo.id == to_do_id).delete()
        db.commit()
