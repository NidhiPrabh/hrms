import os
from functools import lru_cache

class Settings:
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "HRMS"

    # Secret
    SECRET_KEY: str = os.getenv("SECRET_KEY", "dev_secret")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))

    # Database
    SQLALCHEMY_DATABASE_URI: str = os.getenv(
        "DATABASE_URL",
        "sqlite:///./hrms.db?check_same_thread=False"
    )

@lru_cache
def get_settings():
    return Settings()
