from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    telegram_bot_token: str
    openai_api_key: str
    database_url: str = "sqlite:///content_factory.db"

    class Config:
        env_file = ".env"


settings = Settings()
