import sqlalchemy as sa

from models import BaseModel


class Foo(BaseModel):
    __tablename__ = "foo"

    name = sa.Column(sa.String(200), nullable=False)
    description = sa.Column(sa.Text, nullable=True)
    public = sa.Column(sa.Boolean, default=True)
