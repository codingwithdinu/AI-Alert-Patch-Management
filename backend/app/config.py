from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    APP_NAME: str = "AI Alert Patch Management"
    DEBUG: bool = False
    DATABASE_URL: str = "sqlite:///./data/patches.db"
    SMTP_HOST: str = "smtp.gmail.com"
    SMTP_PORT: int = 587
    SMTP_USER: str = ""
    SMTP_PASSWORD: str = ""
    ALERT_FROM_EMAIL: str = ""
    ALERT_TO_EMAIL: str = ""
    SLACK_WEBHOOK_URL: str = ""
    ML_MODEL_PATH: str = "ml/models/risk_model.pkl"

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings() -> Settings:
    return Settings()