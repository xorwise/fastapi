from sqlalchemy.orm import Session
import uuid
from models.foo import Foo
from schemas.foo import FooIn
from utils.exceptions import AppException


def create_foo(db: Session, data: FooIn) -> Foo:
    foo = Foo(**data.model_dump())
    db.add(foo)
    db.commit()
    db.refresh(foo)
    return foo


def get_foos(db: Session) -> list[Foo]:
    return db.query(Foo).all()


def get_foo(db: Session, id: uuid.UUID) -> Foo:
    foo = db.query(Foo).filter(Foo.id == id).first()
    if not foo:
        raise AppException(404, "Foo not found")
    return foo
