from fastapi import HTTPException
from starlette import status

# Exceptions
TO_DO_NOT_FOUND_EXCEPTION = HTTPException(status_code=404, detail="To-do not found")
USER_AUTHENTICATION_EXCEPTION = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Authentication failed",
)
USER_AUTHORIZATION_EXCEPTION = HTTPException(
    status_code=401, detail="Authorization failed"
)
INCORRECT_PASSWORD_EXCEPTION = HTTPException(
    status_code=401, detail="Incorrect password"
)
