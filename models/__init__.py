import uuid
from .foo import Foo, Foo1
from sqlalchemy.orm import declarative_base
import sqlalchemy as sa


Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    id = sa.Column(
        "id",
        sa.UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
    )

    created_at = sa.Column("created_at", sa.TIMESTAMP, server_default=sa.func.now())
    updated_at = sa.Column(
        "updated_at", sa.TIMESTAMP, server_default=sa.func.now(), onupdate=sa.func.now()
    )
