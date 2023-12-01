import json
import datetime as dt
from fastapi import Request, Response

from app.config import settings


async def logging_middleware(request: Request, call_next):
    log = {
        "client_ip": request.client.host,
        "datetime": dt.datetime.utcnow().isoformat(),
        "endpoint": request.url.path,
    }

    response: Response = await call_next(request)

    log["status_code"] = response.status_code

    with open(settings.log_file, "a+") as file:
        file.write(json.dumps(log))
        file.write("\n")

    return response
