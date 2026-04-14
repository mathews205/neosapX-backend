from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

from app.core.config import settings


def create_db_engine() -> Engine:
    return create_engine(
        settings.DATABASE_URL,
        pool_pre_ping=True,
        echo=False,
    )


engine = create_db_engine()