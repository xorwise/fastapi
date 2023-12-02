from pydantic import BaseModel, EmailStr, constr, validator

from app.config import settings


class RegistrationForm(BaseModel):
    first_name: constr(min_length=1)
    last_name: constr(min_length=1)
    password: constr(min_length=8)
    email: EmailStr

    @validator("password")
    def validate_password(cls, password):
        password = settings.PWD_CONTEXT.hash(password)
        return password


class RegistrationSuccess(BaseModel):
    message: str
    access_token: str
