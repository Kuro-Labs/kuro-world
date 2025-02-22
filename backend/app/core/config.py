from typing import List
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Kuro AI API"
    VERSION: str = "0.1.0"
    DESCRIPTION: str = "Modern AI Application API"
    API_V1_STR: str = "/api/v1"
    
    # CORS Configuration
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",  # Next.js frontend
        "http://localhost:8000",  # FastAPI Swagger UI
    ]

    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()
