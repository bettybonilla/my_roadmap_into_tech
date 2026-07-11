from fastapi import HTTPException
from starlette import status

USER_CREATION_EXCEPTION = HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
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
