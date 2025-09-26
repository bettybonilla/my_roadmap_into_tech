from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from .helpers import get_db
from .user_validation import HandleUser

DB_DEPENDENCY = Annotated[Session, Depends(get_db)]
USER_DEPENDENCY = Annotated[dict, Depends(HandleUser.get_current_user)]
