from typing import NoReturn

from fastapi import Request, Path
from jinja2 import TemplateError
from sqlalchemy.exc import SQLAlchemyError
from starlette import status
from starlette.responses import RedirectResponse

from .models import ToDoRequest
from .. import USER_DEPENDENCY, DB_DEPENDENCY
from ..exceptions import USER_AUTHORIZATION_EXCEPTION, TO_DO_NOT_FOUND_EXCEPTION
from ..user_validation import HandleUser
from ... import TEMPLATES
from ...models import ToDo


def redirect_to_login_page():
    redirect_response = RedirectResponse(
        url="/auth/login-page", status_code=status.HTTP_302_FOUND
    )
    redirect_response.delete_cookie(key="access_token")
    return redirect_response


# Pages
async def render_to_do_page_handler(request: Request, db: DB_DEPENDENCY):
    # Get current user
    user = await HandleUser.get_current_user_from_cookies_access_token(request)
    if not user:
        return redirect_to_login_page()

    # Get current user to-dos from database
    try:
        rows = db.query(ToDo).filter(ToDo.owner_id == user.get("user_id")).all()
    except SQLAlchemyError:
        return redirect_to_login_page()

    # Render page
    try:
        # TemplateResponse expects exactly two arguments so it's best to pass a single dictionary instead of multiple
        # dictionaries since it might throw an error or fail silently - Always pass one dictionary containing all your
        # context data
        context = {
            "request": request,
            "user": user,
            "to_dos": rows,
        }
        return TEMPLATES.TemplateResponse("to_do.html", context)
    except TemplateError:
        return redirect_to_login_page()


async def render_add_to_do_page_handler(request: Request):
    user = await HandleUser.get_current_user_from_cookies_access_token(request)
    if not user:
        return redirect_to_login_page()

    try:
        context = {
            "request": request,
            "user": user,
        }
        return TEMPLATES.TemplateResponse("add_to_do.html", context)
    except TemplateError:
        return redirect_to_login_page()


async def render_edit_to_do_page_handler(
    request: Request, db: DB_DEPENDENCY, to_do_id: int = Path(gt=0)
):
    user = await HandleUser.get_current_user_from_cookies_access_token(request)
    if not user:
        return redirect_to_login_page()

    try:
        row = db.query(ToDo).filter(ToDo.id == to_do_id).first()
    except SQLAlchemyError:
        return redirect_to_login_page()

    try:
        context = {
            "request": request,
            "user": user,
            "to_do": row,
        }
        return TEMPLATES.TemplateResponse("edit_to_do.html", context)
    except TemplateError:
        return redirect_to_login_page()


# Endpoints
class UserAccess:
    # Dependent function which depends on the dependency function being passed in the Depends() function - All API
    # endpoints below will be dependent functions
    # The Depends() function is used for dependency injection since it declares that the dependency function being
    # passed in needs to be injected into this dependent function
    # With the Depends() function, FastAPI will automatically call the dependency function being passed in, get the
    # yielded database session, and inject it as the db argument
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
    ) -> ToDo:
        if not user:
            raise USER_AUTHORIZATION_EXCEPTION
        row = (
            db.query(ToDo)
            .filter(ToDo.owner_id == user.get("user_id"))
            .filter(ToDo.id == to_do_id)
            .first()
        )
        if not row:
            raise TO_DO_NOT_FOUND_EXCEPTION
        return row

    @staticmethod
    async def create_to_do_handler(
        user: USER_DEPENDENCY, db: DB_DEPENDENCY, to_do_request: ToDoRequest
    ):
        if not user:
            raise USER_AUTHORIZATION_EXCEPTION
        # For data consistency control, manually unpack data like with create_user_handler in auth/handlers.py file
        row = ToDo(**to_do_request.model_dump(), owner_id=user.get("user_id"))
        # Adds changes to the database session
        db.add(row)
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
        row = (
            db.query(ToDo)
            .filter(ToDo.owner_id == user.get("user_id"))
            .filter(ToDo.id == to_do_id)
            .first()
        )
        if not row:
            raise TO_DO_NOT_FOUND_EXCEPTION
        row.title = to_do_request.title
        row.description = to_do_request.description
        row.priority = to_do_request.priority
        row.complete = to_do_request.complete
        db.add(row)
        db.commit()

    @staticmethod
    async def delete_to_do_handler(
        user: USER_DEPENDENCY, db: DB_DEPENDENCY, to_do_id: int = Path(gt=0)
    ):
        if not user:
            raise USER_AUTHORIZATION_EXCEPTION
        row = (
            db.query(ToDo)
            .filter(ToDo.owner_id == user.get("user_id"))
            .filter(ToDo.id == to_do_id)
            .first()
        )
        if not row:
            raise TO_DO_NOT_FOUND_EXCEPTION
        db.query(ToDo).filter(ToDo.owner_id == user.get("user_id")).filter(
            ToDo.id == to_do_id
        ).delete()
        db.commit()
