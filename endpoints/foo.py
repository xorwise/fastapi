import uuid
from fastapi import APIRouter, Depends
from config.db import get_db
from schemas.foo import FooOut, FooIn
import services


router = APIRouter(prefix="/foo", tags=["foo"])


@router.post("/", response_model=FooOut)
async def create_foo(foo_in: FooIn, db=Depends(get_db)):
    return services.foo.create_foo(db, foo_in)


@router.get("/", response_model=list[FooOut])
async def get_foos(db=Depends(get_db)):
    return services.foo.get_foos(db)


@router.get("/{foo_id}", response_model=FooOut)
async def get_foo(foo_id: uuid.UUID, db=Depends(get_db)):
    return services.foo.get_foo(db, foo_id)
