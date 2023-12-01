from . import BaseSchema
from pydantic import BaseModel


class FooOut(BaseSchema):
    name: str
    description: str


class FooIn(BaseModel):
    name: str
    description: str
