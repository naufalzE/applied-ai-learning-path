from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):



    timeout: int = 30
    app_name: str = "Translate Assistant"

    model_config = SettingsConfigDict(
        env_file=".env"
    )


settings = Settings()