from datetime import datetime

from pydantic import BaseModel, EmailStr, constr


class User(BaseModel):
    first_name: constr(min_length=1)
    last_name: constr(min_length=1)
    email: EmailStr
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class UserAuth(BaseModel):
    email: EmailStr
    password: constr(min_length=8)
