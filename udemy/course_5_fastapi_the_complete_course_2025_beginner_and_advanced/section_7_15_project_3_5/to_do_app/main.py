"""
For this project, we will be able to create to-dos, have a feature to be able to check off the to-dos, and also have a
feature to prioritize them
"""

from fastapi import FastAPI, APIRouter
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from starlette import status

from .database import engine
from .models import Base
from .routers.admin.handlers import AdminAccess
from .routers.auth.handlers import (
    render_login_page_handler,
    render_register_page_handler,
    create_user_handler,
    create_token_handler,
)
from .routers.auth.models import Token
from .routers.to_do.handlers import (
    render_to_do_page_handler,
    render_add_to_do_page_handler,
    render_edit_to_do_page_handler,
    UserAccess,
)
from .routers.user.handlers import (
    get_account_details_handler,
    change_password_handler,
    change_phone_number_handler,
)

app = FastAPI()


@app.get("/")
def test():
    return RedirectResponse(url="/to-dos/to-do-page", status_code=status.HTTP_302_FOUND)


@app.get("/health-check")
def health_check() -> dict[str, str]:
    return {"status": "healthy"}


# The APIRouter instances along with app.include_router(APIRouter instance) allow you to spin up your server with this
# main.py file and keep separate files for the routers logic while running on the same port which makes our FastAPI
# application (backend server) scalable + maintainable
# The prefix="/to-dos" parameter sets each API endpoint in the to-do routes to be prefixed with "/to-dos"
# The tags=["to-do"] parameter separates the to-do related API endpoints in the Swagger UI
to_do_router = APIRouter(prefix="/to-dos", tags=["to-do"])
auth_router = APIRouter(prefix="/auth", tags=["auth"])
admin_router = APIRouter(prefix="/admin", tags=["admin"])
user_router = APIRouter(prefix="/user", tags=["user"])
# Creates the SQLite database (to_do_app.db file) automagically in the app directory along with this main.py file when
# you spin up your server with this main.py file which uses the database URL in the database.py file - This line of code
# below will not run or update your table schemas in your SQLite database file if it already exists therefore, you need
# to delete your SQLite database file if you modify the table schemas in your models.py file in order to re-run this
# line of code below to re-create and update your SQLite database file with your modifications however you also have to
# re-create all the data in your tables from scratch since you deleted your previous SQLite database file
# After you run the line of code below, you can kill your server
# Then you can use the sqlite3 to_do_app.db command to start using SQLite with your SQLite database
# The .schema command can be used to view an overview of all your tables in your SQLite database
# You can change the view of your tables using the following commands:
# - .mode column (Best view for a lot of columns)
# - .mode markdown
# - .mode box (My favorite view for a few columns)
# - .mode table
Base.metadata.create_all(bind=engine)
app.mount("/static", StaticFiles(directory="to_do_app/static"), name="static")

# TO-DO ROUTES ---------------------------------------------------------------------------------------------------------
# To-do pages
to_do_router.get("/to-do-page", status_code=status.HTTP_200_OK)(
    render_to_do_page_handler
)
to_do_router.get("/add-to-do-page", status_code=status.HTTP_200_OK)(
    render_add_to_do_page_handler
)
to_do_router.get("/edit-to-do-page/{to_do_id}", status_code=status.HTTP_200_OK)(
    render_edit_to_do_page_handler
)
# To-do endpoints
to_do_router.get("/", response_model=None, status_code=status.HTTP_200_OK)(
    UserAccess.read_all_to_dos_handler
)
to_do_router.get("/{to_do_id}", response_model=None, status_code=status.HTTP_200_OK)(
    UserAccess.read_to_do_handler
)
to_do_router.post("/create-to-do", status_code=status.HTTP_201_CREATED)(
    UserAccess.create_to_do_handler
)
to_do_router.put("/update-to-do/{to_do_id}", status_code=status.HTTP_204_NO_CONTENT)(
    UserAccess.update_to_do_handler
)
to_do_router.delete("/delete-to-do/{to_do_id}", status_code=status.HTTP_204_NO_CONTENT)(
    UserAccess.delete_to_do_handler
)
# AUTH ROUTES ----------------------------------------------------------------------------------------------------------
# Auth pages
auth_router.get("/login-page", status_code=status.HTTP_200_OK)(
    render_login_page_handler
)
auth_router.get("/register-page", status_code=status.HTTP_200_OK)(
    render_register_page_handler
)
# Auth endpoints
auth_router.post("/create-user", status_code=status.HTTP_201_CREATED)(
    create_user_handler
)
auth_router.post(
    "/create-token", response_model=Token, status_code=status.HTTP_201_CREATED
)(create_token_handler)
# ADMIN ROUTES ---------------------------------------------------------------------------------------------------------
# Admin endpoints
admin_router.get("/to-dos", response_model=None, status_code=status.HTTP_200_OK)(
    AdminAccess.read_all_to_dos_handler
)
admin_router.delete(
    "/to-dos/delete-to-do/{to_do_id}", status_code=status.HTTP_204_NO_CONTENT
)(AdminAccess.delete_to_do_handler)
# USER ROUTES ----------------------------------------------------------------------------------------------------------
# User endpoints
user_router.get(
    "/account-details", response_model=None, status_code=status.HTTP_200_OK
)(get_account_details_handler)
user_router.put(
    "/change-password", response_model=None, status_code=status.HTTP_204_NO_CONTENT
)(change_password_handler)
user_router.put(
    "/change-phone-number", response_model=None, status_code=status.HTTP_204_NO_CONTENT
)(change_phone_number_handler)

app.include_router(to_do_router)
app.include_router(auth_router)
app.include_router(admin_router)
app.include_router(user_router)
