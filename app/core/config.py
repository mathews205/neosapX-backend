from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    APP_ENV: str = "dev"

    # Individual fields (useful for debugging & flexibility)
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_NAME: str = "neosapx"
    DB_USER: str = "neosapx_user"
    DB_PASSWORD: str = ""

    # Single DSN (what SQLAlchemy actually needs)
    DATABASE_URL: str

settings = Settings()