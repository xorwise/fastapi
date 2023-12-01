from fastapi import FastAPI
from config import settings
from endpoints import foo
import uvicorn

from utils.exceptions import AppException, app_exception_handler


app = FastAPI(docs_url="/api/v1/docs", version="1.0")
app.include_router(foo.router, prefix=settings.path_prefix)

app.add_exception_handler(AppException, app_exception_handler)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
