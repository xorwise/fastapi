from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from pydantic.v1 import BaseSettings
#from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv(".env")


class Settings(BaseSettings):
    app_host: str = "0.0.0.0"
    app_port: int = 8000
    path_prefix: str = "/api/v1"
    database_url: str
    celery_broker_url: str
    celery_result_backend: str
    log_file: str = "server.log"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440
    PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")
    OAUTH2_SCHEME = OAuth2PasswordBearer(tokenUrl="/api/v1/user/authentication")
    SECRET_KEY: str = ""
    ALGORITHM: str = "HS256"


settings = Settings()
