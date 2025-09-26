import os
from typing import Iterator

from ..database import SessionLocal


# Dependency function
# Yields a database session - This is also a generator function
def get_db() -> Iterator[SessionLocal]:
    db = SessionLocal()
    try:
        # Yields the database session to be used by the dependent function
        # This allows us to connect and contact our local database
        yield db
    finally:
        # Ensures the database session is closed after the request
        db.close()


# Returns the exported environ_var variable from the profile file (bash profile/os) which should be used in production
# for security purposes since it won't be committed
# Otherwise, returns the default_value variable which should be used for testing purposes only since it will be
# committed however it won't be used in production
def get_exported_environ_var(environ_var: str, default_value: str) -> str:
    exported_environ_var = os.getenv(environ_var)
    if not exported_environ_var:
        return default_value
    return exported_environ_var
