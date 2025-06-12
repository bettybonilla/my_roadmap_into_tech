"""
For this project, we will be able to create to-dos, have a feature to be able to check off the to-dos, and also have a
feature to prioritize them
"""

from fastapi import FastAPI, APIRouter
from starlette import status

import models
from database import engine
from routers.admin.admin_handlers import AdminAccess
from routers.auth.auth_handlers import create_user_handler, create_token_handler
from routers.auth.auth_models import Token
from routers.to_do.to_do_handlers import UserAccess
from routers.user.user_handlers import get_account_details, change_password

app = FastAPI()
# The APIRouter instances along with app.include_router(APIRouter instance) allow you to spin up your server with this
# main.py file and keep separate files for the routers logic while running on the same port which makes our FastAPI
# application (backend server) scalable + maintainable
# The prefix="/user" parameter sets each API endpoint in the to-do routes to be prefixed with "/user"
# The tags=["to-do"] parameter separates the to-do related API endpoints in the Swagger UI
to_do_router = APIRouter(prefix="/user", tags=["to-do"])
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
models.Base.metadata.create_all(bind=engine)

# To-do routes
to_do_router.get("/to-dos", response_model=None, status_code=status.HTTP_200_OK)(
    UserAccess.read_all_to_dos_handler
)
to_do_router.get(
    "/to-dos/{to_do_id}", response_model=None, status_code=status.HTTP_200_OK
)(UserAccess.read_to_do_handler)
to_do_router.post("/create-to-do", status_code=status.HTTP_201_CREATED)(
    UserAccess.create_to_do_handler
)
to_do_router.put("/update-to-do/{to_do_id}", status_code=status.HTTP_204_NO_CONTENT)(
    UserAccess.update_to_do_handler
)
to_do_router.delete("/delete-to-do/{to_do_id}", status_code=status.HTTP_204_NO_CONTENT)(
    UserAccess.delete_to_do_handler
)

# Auth routes
auth_router.post("/create-user", status_code=status.HTTP_201_CREATED)(
    create_user_handler
)
auth_router.post(
    "/create-token", response_model=Token, status_code=status.HTTP_201_CREATED
)(create_token_handler)

# Admin routes
admin_router.get("/to-dos", response_model=None, status_code=status.HTTP_200_OK)(
    AdminAccess.read_all_to_dos_handler
)
admin_router.delete("/delete-to-do/{to_do_id}", status_code=status.HTTP_204_NO_CONTENT)(
    AdminAccess.delete_to_do_handler
)

# User routes
user_router.get(
    "/account-details", response_model=None, status_code=status.HTTP_200_OK
)(get_account_details)
user_router.put(
    "/change-password", response_model=None, status_code=status.HTTP_204_NO_CONTENT
)(change_password)

app.include_router(to_do_router)
app.include_router(auth_router)
app.include_router(admin_router)
app.include_router(user_router)
