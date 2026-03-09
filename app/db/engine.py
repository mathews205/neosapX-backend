from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

from app.core.config import settings


def create_db_engine() -> Engine:
    # pool_pre_ping: checks stale connections and refreshes them (helps in dev/prod)
    return create_engine(
        settings.DATABASE_URL,
        pool_pre_ping=True,
        echo=False,  # set True temporarily if you want to see SQL logs
    )


engine = create_db_engine()