from datetime import timedelta, datetime, timezone
from typing import Literal, Annotated, Optional

from fastapi import Request, Depends, HTTPException
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from .config import BCRYPT_CONTEXT, ALGORITHM, SECRET, OAUTH2_BEARER
from .exceptions import USER_AUTHENTICATION_EXCEPTION
from ..models import User


class HandleUser:
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

    # Creates and returns the access token as the encoded JWT
    @staticmethod
    def create_access_token(
        username: str, user_id: int, user_role: str, expires_delta: timedelta
    ) -> str:
        payload = {"sub": username, "id": user_id, "role": user_role}
        expires = datetime.now(timezone.utc) + expires_delta
        payload.update({"exp": expires})
        encoded_jwt = jwt.encode(algorithm=ALGORITHM, claims=payload, key=SECRET)
        return encoded_jwt

    # Returns the current user after getting the access token from cookies
    @staticmethod
    async def get_current_user_from_cookies_access_token(
        request: Request,
    ) -> Optional[dict[str, str | int]]:
        token = request.cookies.get("access_token")
        if not token:
            return None

        try:
            user = await HandleUser.get_current_user(token)
        except HTTPException:
            return None
        return user

    # Dependent function and dependency function
    # Returns the current user as the decoded JWT
    @staticmethod
    async def get_current_user(
        token: Annotated[str, Depends(OAUTH2_BEARER)],
    ) -> dict[str, str | int]:
        """
        Decode the JWT of the current user.

        :param token: JWT of the current user
        :return: {"username": username, "user_id": user_id, "user_role": user_role}
        :raises USER_AUTHENTICATION_EXCEPTION
        """
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
        if not username or not user_id or not user_role:
            raise USER_AUTHENTICATION_EXCEPTION
        return {"username": username, "user_id": user_id, "user_role": user_role}
