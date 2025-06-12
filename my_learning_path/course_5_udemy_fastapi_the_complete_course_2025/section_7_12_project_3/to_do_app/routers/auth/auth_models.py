from pydantic import BaseModel, EmailStr, Field


class CreateUserRequest(BaseModel):
    email: EmailStr
    username: str = Field(min_length=3)
    first_name: str = Field(min_length=3)
    last_name: str = Field(min_length=3)
    password: str = Field(min_length=7)
    role: str


class Token(BaseModel):
    access_token: str
    token_type: str
