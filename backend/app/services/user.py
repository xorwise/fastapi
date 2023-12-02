from datetime import datetime, timedelta

from fastapi import Depends
from jose import JWTError, jwt
from starlette import status


from app.config import settings, get_session
from app.schemas.token import TokenData


from sqlalchemy import delete, exc, select
from sqlalchemy.orm import Session
from starlette.status import HTTP_409_CONFLICT
from app.models import User
from app.schemas.registration import RegistrationForm
from fastapi import HTTPException


async def get_user(session: Session, email: str) -> User | None:
    query = select(User).where(User.email == email)
    return session.scalar(query)


async def register_user(session: Session, potential_user: RegistrationForm) -> tuple[bool, str]:
    user = User(**potential_user.dict(exclude_unset=True))
    session.add(user)
    try:
        session.commit()
    except exc.IntegrityError:
        raise HTTPException(status_code=HTTP_409_CONFLICT, detail="User with provided email already exists")
    return True, "Successful registration!", user.email


async def delete_user(session: Session, email: str) -> None:
    query = delete(User).where(User.email == email)
    session.execute(query)
    session.commit()


async def authenticate_user(session: Session, email: str, password: str):
    user = await get_user(session, email)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(
    data: dict,
    expires_delta: timedelta | None = None,
):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_jwt


def verify_password(
    plain_password: str,
    hashed_password: str,
):
    pwd_context = settings.PWD_CONTEXT
    return pwd_context.verify(plain_password, hashed_password)


async def get_current_user(
    session: Session = Depends(get_session),
    token: str = Depends(settings.OAUTH2_SCHEME),
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception
    user = await get_user(session, email=token_data.email)
    if user is None:
        raise credentials_exception
    return user


def get_user_by_id(session: Session, user_id: int) -> User | None:
    return session.query(User).filter(User.id == user_id).first()
