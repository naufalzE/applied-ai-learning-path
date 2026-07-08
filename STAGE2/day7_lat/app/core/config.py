from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    llm_api_key: str
    llm_base_url: str

    timeout: int = 30
    app_name: str = "Translate Assistant"

    model_config = SettingsConfigDict(
        env_file=".env"
    )


settings = Settings()