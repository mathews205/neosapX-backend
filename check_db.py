from sqlalchemy import text

from app.db.engine import engine

with engine.connect() as conn:
    result = conn.execute(text("SELECT 1")).scalar_one()
    print("DB OK, SELECT 1 ->", result)