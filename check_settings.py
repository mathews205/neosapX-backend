from app.core.config import settings

print("ENV:", settings.APP_ENV)
print("DB:", settings.DB_HOST, settings.DB_PORT, settings.DB_NAME)
print("URL:", settings.DATABASE_URL)  # safe; password will be URL-encoded