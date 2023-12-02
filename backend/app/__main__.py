import uvicorn
from fastapi import FastAPI
from fastapi_pagination import add_pagination
from app.config import init_db, settings

from app.endpoints import list_of_routes

from app.utils.exceptions import AppException, app_exception_handler
from app.utils.logger import logging_middleware


def bind_routes(application: FastAPI, setting: settings) -> None:
    """
    Bind all routes to application.
    """
    for route in list_of_routes:
        application.include_router(route, prefix=setting.path_prefix)


def connect_middlewares(application: FastAPI) -> None:
    application.middleware("http")(logging_middleware)


def get_app() -> FastAPI:
    """
    Creates application and all dependable objects.
    """
    description = "App"

    tags_metadata = [
        {
            "name": "Application Health",
            "description": "API health check.",
        },
    ]

    application = FastAPI(
        title="Application",
        description=description,
        docs_url="/api/swagger",
        openapi_url="/api/openapi",
        version="0.1.0",
        openapi_tags=tags_metadata,
    )
    bind_routes(application, settings)
    connect_middlewares(application)
    add_pagination(application)
    application.add_exception_handler(AppException, app_exception_handler)
    application.state.settings = settings
    application.add_event_handler("startup", init_db)
    return application


app = get_app()


if __name__ == "__main__":
    uvicorn.run(
        app,
        host=settings.app_host,
        port=settings.app_port,
        log_level="debug"
    )
