from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv(".env")


class Settings(BaseSettings):
    path_prefix: str = "/api/v1"
    database_url: str
    celery_broker_url: str
    celery_result_backend: str
    log_file: str = "server.log"


settings = Settings()
