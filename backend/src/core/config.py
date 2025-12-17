from pydantic_settings import SettingsConfigDict, BaseSettings
import os
from typing import Optional


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore"
    )
    
    # Application settings
    APP_NAME: str = "Docusaurus RAG Chatbot API"
    APP_VERSION: str = "1.0.0"
    
    # Qdrant settings
    QDRANT_URL: str = os.getenv("QDRANT_URL", "https://your-cluster-url.qdrant.io:6333")
    QDRANT_API_KEY: str = os.getenv("QDRANT_API_KEY", "")
    QDRANT_COLLECTION_NAME: str = os.getenv("QDRANT_COLLECTION_NAME", "book_embeddings")
    
    # Neon Postgres settings
    NEON_DATABASE_URL: str = os.getenv("NEON_DATABASE_URL", "")
    
    # OpenAI settings
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
    
    # Other settings
    CORS_ORIGINS: str = os.getenv("CORS_ORIGINS", "*")


settings = Settings()