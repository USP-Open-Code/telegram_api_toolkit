from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    TELEGRAM_KEY: str
    RESPONSE_ENDPOINT: str

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
