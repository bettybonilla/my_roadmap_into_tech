from datetime import timedelta, datetime, timezone
from typing import Literal, Annotated

from fastapi import Depends
from fastapi import HTTPException
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from starlette import status

from . import BCRYPT_CONTEXT, ALGORITHM, SECRET, OAUTH2_BEARER
from ...models import User

USER_AUTHENTICATION_EXCEPTION = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication failed"
)


class UserValidation:
    # Authenticates the user login
    @staticmethod
    def authenticate_user_login(
        username: str, password: str, db: Session
    ) -> User | Literal[False]:
        user = db.query(User).filter(User.username == username).first()
        if not user:
            return False
        if not BCRYPT_CONTEXT.verify(password, user.hashed_password):
            return False
        return user

    # Returns the access token as the encoded JWT
    @staticmethod
    def get_access_token(
        username: str, user_id: int, user_role: str, expires_delta: timedelta
    ) -> str:
        payload = {"sub": username, "id": user_id, "role": user_role}
        expires = datetime.now(timezone.utc) + expires_delta
        payload.update({"exp": expires})
        encoded_jwt = jwt.encode(algorithm=ALGORITHM, claims=payload, key=SECRET)
        return encoded_jwt

    # Dependent function and dependency function
    # Returns the decoded JWT of the current user
    @staticmethod
    async def get_current_user(
        token: Annotated[str, Depends(OAUTH2_BEARER)],
    ) -> dict[str, str | int]:
        try:
            payload = jwt.decode(token, algorithms=ALGORITHM, key=SECRET)
        except JWTError:
            raise USER_AUTHENTICATION_EXCEPTION

        try:
            expires = payload.get("exp")
            expires = datetime.fromtimestamp(expires, tz=timezone.utc)
            now = datetime.now(timezone.utc)
            if now >= expires:
                raise USER_AUTHENTICATION_EXCEPTION
        except ValueError:
            raise USER_AUTHENTICATION_EXCEPTION
        except TypeError:
            raise USER_AUTHENTICATION_EXCEPTION

        username: str = payload.get("sub")
        user_id: int = payload.get("id")
        user_role: str = payload.get("role")
        if not username or not user_id:
            raise USER_AUTHENTICATION_EXCEPTION
        return {"username": username, "user_id": user_id, "user_role": user_role}
