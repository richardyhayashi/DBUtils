from pydantic import BaseSettings

class Settings(BaseSettings):
    """Contains all the settings for the application."""
    db_dialect: str
    db_username: str
    db_password: str
    db_host: str 
    db_port: int
    db_name: str

    class Config:
        """Loads environment variables from env_file"""
        env_file = 'config/.env'
        env_file_encoding = 'utf-8'
