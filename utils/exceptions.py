from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse


class AppException(HTTPException):
    def __init__(self, status_code: int, detail: str):
        super().__init__(status_code=status_code, detail=detail)

    def __str__(self):
        return f"{self.status_code} - {self.detail}"


async def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})
