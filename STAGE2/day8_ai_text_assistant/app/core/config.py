from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME : str
    LLM_API_KEY : str
    LLM_BASE_URL : str
    TIMEOUT : int
    DEBUG : bool
    
    model_config = SettingsConfigDict(
        env_file= ".env",
        env_file_encoding= "utf-8"
    )

settings = Settings()