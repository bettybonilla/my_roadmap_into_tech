from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

from ..helpers import get_exported_environ_var

# Used for hashing passwords
# The below is the setup for passlib to work properly
BCRYPT_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Used to create the JWT:
# HS256 is a symmetric cryptographic algorithm used to digitally sign a JWT
ALGORITHM = "HS256"
# The default value str was generated in terminal using the openssl rand -hex 32 command which can be used to generate
# pseudo-random bytes
SECRET = get_exported_environ_var(
    "JWT_SECRET", "742dae3759bef4750a8e2ea26a22df829ec867c57f33bf049de8c59ae8dd41cc"
)

# Used for dependency injection to decode the JWT of the current user
OAUTH2_BEARER = OAuth2PasswordBearer(tokenUrl="auth/create-token")
