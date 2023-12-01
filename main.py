from fastapi import FastAPI
from config import settings
from config.db import init_db
from endpoints import foo
import uvicorn

from utils.exceptions import AppException, app_exception_handler
from utils.logger import logging_middleware


app = FastAPI(docs_url="/api/v1/docs", version="1.0")
app.include_router(foo.router, prefix=settings.path_prefix)

app.add_exception_handler(AppException, app_exception_handler)
app.add_middleware(logging_middleware)

app.add_event_handler("startup", init_db)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
