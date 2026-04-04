from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    app_name: str = "recover-data-service"
    app_env: str = "development"
    port: int = 8001

    database_url: str = "postgresql+asyncpg://user:password@localhost:5432/recover"


settings = Settings()
