from pydantic import BaseModel, ConfigDict
from datetime import datetime
import uuid


class BaseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
