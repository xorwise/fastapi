import sqlalchemy as sa

from app.models import BaseModel


class User(BaseModel):
    __tablename__ = "User"

    first_name = sa.Column(
        sa.Text,
        nullable=False
    )

    last_name = sa.Column(
        sa.Text,
        nullable=False
    )

    password = sa.Column(
        sa.Text,
        nullable=False
    )

    email = sa.Column(
        sa.Text,
        nullable=False,
        unique=True
    )
