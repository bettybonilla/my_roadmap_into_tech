from typing import Annotated, NoReturn, Optional

from fastapi import Depends, Path
from models import ToDo
from routers import TO_DO_NOT_FOUND_EXCEPTION, USER_AUTHORIZATION_EXCEPTION
from routers.auth.auth_user_validation import UserValidation
from routers.helpers import get_db
from routers.to_do.to_do_models import ToDoRequest
from sqlalchemy.orm import Session

DB_DEPENDENCY = Annotated[Session, Depends(get_db)]
USER_DEPENDENCY = Annotated[dict, Depends(UserValidation.get_current_user)]


class UserAccess:
    # Dependent function which depends on the dependency function being passed in the Depends() function - All API endpoints
    # below will be dependent functions
    # The Depends() function is used for dependency injection since it declares that the dependency function being passed in
    # needs to be injected into this dependent function
    # With the Depends() function, FastAPI will automatically call the dependency function being passed in, get the yielded
    # database session, and inject it as the db argument
    @staticmethod
    async def read_all_to_dos_handler(
        user: USER_DEPENDENCY, db: DB_DEPENDENCY
    ) -> list[ToDo | NoReturn]:
        if not user:
            raise USER_AUTHORIZATION_EXCEPTION
        return db.query(ToDo).filter(ToDo.owner_id == user.get("user_id")).all()

    @staticmethod
    async def read_to_do_handler(
        user: USER_DEPENDENCY, db: DB_DEPENDENCY, to_do_id: int = Path(gt=0)
    ) -> Optional[ToDo]:
        if not user:
            raise USER_AUTHORIZATION_EXCEPTION
        to_dos_table = (
            db.query(ToDo)
            .filter(ToDo.owner_id == user.get("user_id"))
            .filter(ToDo.id == to_do_id)
            .first()
        )
        if not to_dos_table:
            raise TO_DO_NOT_FOUND_EXCEPTION
        return to_dos_table

    @staticmethod
    async def create_to_do_handler(
        user: USER_DEPENDENCY, db: DB_DEPENDENCY, to_do_request: ToDoRequest
    ):
        if not user:
            raise USER_AUTHORIZATION_EXCEPTION
        to_dos_table = ToDo(**to_do_request.model_dump(), owner_id=user.get("user_id"))
        # Adds changes to the database session
        db.add(to_dos_table)
        # Commits changes to the database session
        db.commit()

    @staticmethod
    async def update_to_do_handler(
        user: USER_DEPENDENCY,
        db: DB_DEPENDENCY,
        to_do_request: ToDoRequest,
        to_do_id: int = Path(gt=0),
    ):
        if not user:
            raise USER_AUTHORIZATION_EXCEPTION
        to_dos_table = (
            db.query(ToDo)
            .filter(ToDo.owner_id == user.get("user_id"))
            .filter(ToDo.id == to_do_id)
            .first()
        )
        if not to_dos_table:
            raise TO_DO_NOT_FOUND_EXCEPTION
        to_dos_table.title = to_do_request.title
        to_dos_table.description = to_do_request.description
        to_dos_table.priority = to_do_request.priority
        to_dos_table.complete = to_do_request.complete
        db.add(to_dos_table)
        db.commit()

    @staticmethod
    async def delete_to_do_handler(
        user: USER_DEPENDENCY, db: DB_DEPENDENCY, to_do_id: int = Path(gt=0)
    ):
        if not user:
            raise USER_AUTHORIZATION_EXCEPTION
        to_dos_table = (
            db.query(ToDo)
            .filter(ToDo.owner_id == user.get("user_id"))
            .filter(ToDo.id == to_do_id)
            .first()
        )
        if not to_dos_table:
            raise TO_DO_NOT_FOUND_EXCEPTION
        db.query(ToDo).filter(ToDo.owner_id == user.get("user_id")).filter(
            ToDo.id == to_do_id
        ).delete()
        db.commit()
