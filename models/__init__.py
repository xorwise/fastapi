from .base import BaseModel, Base
from .foo import Foo

metadata = [model.metadata for model in Base.__subclasses__()]
