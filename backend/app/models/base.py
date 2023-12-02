import uuid
from app.config import Base
import sqlalchemy as sa


class BaseModel(Base):
    __abstract__ = True

    id = sa.Column(
        "id",
        sa.UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
        unique=True,
        nullable=False
    )

    created_at = sa.Column(
        "created_at",
        sa.TIMESTAMP,
        server_default=sa.func.now(),
        nullable=False
    )

    updated_at = sa.Column(
        "updated_at",
        sa.TIMESTAMP,
        server_default=sa.func.now(),
        onupdate=sa.func.now(),
        nullable=False
    )
