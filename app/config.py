from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "LifeOS"
    debug: bool = False
    database_url: str = "sqlite:///./lifeos.db"


settings = Settings()
