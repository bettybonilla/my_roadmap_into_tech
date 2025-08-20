from typing import Iterator

import pytest
from sqlalchemy import text

from . import TestSessionLocal, engine
from ..models import ToDo, User
from ..routers.auth import BCRYPT_CONTEXT


# Dependency function
# Yields a database session - This is also a generator function
def mock_get_db() -> Iterator[TestSessionLocal]:
    db = TestSessionLocal()
    try:
        yield db
    finally:
        db.close()


# Dependent function and dependency function
# Returns the decoded JWT of the current user
def mock_get_current_user() -> dict[str, str | int]:
    return {"username": "codingwithroby", "user_id": 1, "user_role": "admin"}


# The yield keyword is being used as a control-flow trick that lets pytest run the setup phase before the yield keyword,
# then stops execution until the test function calling this fixture exits, and then run the rest of the teardown/cleanup
# phase
@pytest.fixture
def mock_to_dos_table():
    # Setup phase
    to_dos_table = ToDo(
        title="Learn to code!",
        description="Need to learn everyday!",
        priority=5,
        complete=False,
        owner_id=1,
    )
    db = TestSessionLocal()
    db.add(to_dos_table)
    db.commit()
    # Stops execution until the test function calling this fixture exits
    yield to_dos_table
    # Teardown/cleanup phase
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM to_dos;"))
        connection.commit()


@pytest.fixture
def mock_users_table():
    users_table = User(
        email="codingwithroby@email.com",
        username="codingwithroby",
        first_name="Eric",
        last_name="Roby",
        hashed_password=BCRYPT_CONTEXT.hash("testpassword"),
        role="admin",
        phone_number="111-111-1111",
    )
    db = TestSessionLocal()
    db.add(users_table)
    db.commit()
    yield users_table
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM users;"))
        connection.commit()
