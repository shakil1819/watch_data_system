from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://user:password@localhost/watchdb"
    REDIS_URL: str = "redis://localhost:6379"
    OPENAI_API_KEY: str = "your-openai-api-key"
    CHROMA_PERSIST_DIRECTORY: str = "./chroma_db"

    class Config:
        env_file = ".env"

settings = Settings()
