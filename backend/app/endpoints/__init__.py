from .ping import api_router as Ping
from .auth import api_router as auth_router


list_of_routes = [
    Ping,
    auth_router
]


__all__ = [
    "list_of_routes"
]
