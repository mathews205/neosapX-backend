from sqlalchemy import text
from app.db.engine import engine


with engine.connect() as connection:
    result = connection.execute(text("SELECT 1"))
    print("DB connection successful:", result.scalar())