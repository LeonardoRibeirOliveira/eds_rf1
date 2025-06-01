from pydantic import BaseSettings

class Settings(BaseSettings):
    OPENWEATHER_API_KEY: str
    GEOCODING_PROVIDER: str = "nominatim"
    
    class Config:
        env_file = ".env"

settings = Settings()