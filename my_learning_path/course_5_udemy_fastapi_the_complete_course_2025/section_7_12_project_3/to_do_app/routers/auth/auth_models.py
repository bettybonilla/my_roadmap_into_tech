from pydantic import BaseModel, EmailStr, Field


class CreateUserRequest(BaseModel):
    email: EmailStr
    username: str = Field(min_length=3)
    first_name: str = Field(min_length=3)
    last_name: str = Field(min_length=3)
    password: str = Field(min_length=7)
    role: str
    phone_number: str = Field(min_length=10)


class Token(BaseModel):
    access_token: str
    token_type: str
