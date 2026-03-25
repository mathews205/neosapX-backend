from typing import Generator

from sqlalchemy.orm import sessionmaker

from app.db.engine import engine

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
)
