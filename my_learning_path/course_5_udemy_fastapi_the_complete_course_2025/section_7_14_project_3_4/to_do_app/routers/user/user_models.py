from pydantic import BaseModel, Field


class ChangePasswordRequest(BaseModel):
    current_password: str
    new_password: str = Field(min_length=7)


class ChangePhoneNumberRequest(BaseModel):
    new_phone_number: str = Field(min_length=10)
