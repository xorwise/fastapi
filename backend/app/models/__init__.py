from .base import BaseModel, Base
from .user import User

metadata = [model.metadata for model in Base.__subclasses__()]
