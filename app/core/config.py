from urllib.parse import quote_plus
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
    DB_SCHEMA: str = "app"

    @property
    def DATABASE_URL(self) -> str:
        pwd = quote_plus(self.DB_PASSWORD)
        return (
            f"postgresql+psycopg://{self.DB_USER}:{pwd}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
            f"?options=-csearch_path%3D{self.DB_SCHEMA}"
        )


settings = Settings()