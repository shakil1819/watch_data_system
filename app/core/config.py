from pydantic import Field, validator
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    pg_url: str = Field(..., env='pg_url')
    # REDIS_URL: str = Field("redis://localhost:6379", env='REDIS_URL')
    # OPENAI_API_KEY: str = Field("your-openai-api-key", env='OPENAI_API_KEY')
    # CHROMA_PERSIST_DIRECTORY: str = Field("./chroma_db", env='CHROMA_PERSIST_DIRECTORY')
    scrapingdog_api_key: str = Field(..., env='scrapingdog_api_key')
    POSTGRES_USER: str = Field(..., env='POSTGRES_USER')
    POSTGRES_PASSWORD: str = Field(..., env='POSTGRES_PASSWORD')
    POSTGRES_DB: str = Field(..., env='POSTGRES_DB')
    POSTGRES_PORT: str = Field(..., env='POSTGRES_PORT')
    PGADMIN_DEFAULT_EMAIL: str = Field(..., env='PGADMIN_DEFAULT_EMAIL')
    PGADMIN_DEFAULT_PASSWORD: str = Field(..., env='PGADMIN_DEFAULT_PASSWORD')
    OXYLAB_USERNAME: str = Field(..., env='OXYLAB_USERNAME')
    OXYLAB_PASSWORD: str = Field(..., env='OXYLAB_PASSWORD')

    @validator('pg_url', pre=True, always=True)
    def validate_pg_url(cls, v):
        if not v:
            raise ValueError('pg_url must be provided')
        return v

    class Config:
        env_file = ".env"
        extra = "allow"
settings = Settings()
