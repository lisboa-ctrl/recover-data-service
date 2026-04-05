import os

from pydantic_settings import BaseSettings, SettingsConfigDict

_app_env = os.environ.get("APP_ENV", "development")


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env", f".env.{_app_env}"),
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "recover-data-service"
    app_env: str = "development"
    port: int = 8001

    database_url: str = "postgresql+asyncpg://user:password@localhost:5432/recover"


settings = Settings()
