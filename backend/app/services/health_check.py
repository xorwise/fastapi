from sqlalchemy.orm import Session
from sqlalchemy import select, text


async def health_check_db(db: Session) -> bool:
    query = select(text("1"))
    result = db.scalar(query)
    return result is not None
