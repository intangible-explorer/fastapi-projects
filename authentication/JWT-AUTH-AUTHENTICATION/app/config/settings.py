from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCCESS_TOKEN_EXPIRY_MINS: int = 15
    REFRESH_TOKEN_EXPIRY_DAYS: int = 1


    class Config:
        env_file = ".env"

@lru_cache
def get_settings():
    return Settings()