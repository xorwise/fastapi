from fastapi import FastAPI
from app.config import settings
from app.config.db import init_db
from app.endpoints import foo
import uvicorn

from app.utils.exceptions import AppException, app_exception_handler
from app.utils.logger import logging_middleware


app = FastAPI(docs_url="/api/v1/docs", version="1.0")
app.include_router(foo.router, prefix=settings.path_prefix)

app.add_exception_handler(AppException, app_exception_handler)
app.middleware("http")(logging_middleware)

app.add_event_handler("startup", init_db)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
