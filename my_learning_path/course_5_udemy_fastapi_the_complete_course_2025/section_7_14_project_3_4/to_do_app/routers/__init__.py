from typing import Annotated

from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status

from .auth.auth_user_validation import UserValidation
from .helpers import get_db

# Dependencies
DB_DEPENDENCY = Annotated[Session, Depends(get_db)]
USER_DEPENDENCY = Annotated[dict, Depends(UserValidation.get_current_user)]

# Exceptions
USER_AUTHENTICATION_EXCEPTION = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication failed"
)
USER_AUTHORIZATION_EXCEPTION = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED, detail="Authorization failed"
)
INCORRECT_PASSWORD_EXCEPTION = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password"
)
USER_FORBIDDEN_EXCEPTION = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden request"
)
TO_DO_NOT_FOUND_EXCEPTION = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="To-do not found"
)
