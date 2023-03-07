"""
FastAPI server configuration
"""

# pylint: disable=too-few-public-methods
import secrets
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

from urllib.parse import quote_plus  
from decouple import AutoConfig, RepositoryEnv, Config
from pydantic import BaseModel, AnyHttpUrl, PostgresDsn, validator

DEV_ENV = ".dev.env"
STG_ENV = ".stg.env"
PROD_ENV = ".env"

def __get_config() -> Config:
    if Path(DEV_ENV).exists():
        print("Loading .dev.env........")
        return Config(RepositoryEnv(".dev.env"))
    elif Path(STG_ENV).exists():
        print("Loading .stg.env........")
        return Config(RepositoryEnv(".stg.env"))
    elif Path(PROD_ENV).exists():
        print("Loading .env........")
        return Config(RepositoryEnv(".env"))
    

config = __get_config()

class Settings(BaseModel):
    """Server config settings"""
    PROJECT_NAME = config("PROJECT_NAME")

    mysql_username = config("MYSQL_USERNAME")
    mysql_password = quote_plus(config("MYSQL_PASSWORD"))
    mysql_server = config("MYSQL_SERVER")
    mysql_port = config("MYSQL_PORT")
    mysql_db = config("MYSQL_DB")
    MYSQL_URI = f"mysql://{mysql_username}:{mysql_password}@{mysql_server}/{mysql_db}?ssl=false"
    

    # Security settings
    SECRET_KEY = secrets.token_urlsafe(32)
    AUTHJWT_SECRET_KEY = config("SECRET_KEY")
    SALT = config("SALT").encode()
    
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8


    # API server settings
    API_V1_STR = config("API_V1_STR", default="/api/v1")
    
    # Openapi key
    OPEN_API_KEY = config("open_api_key")
    
    
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)
    
    TESTING = config("TESTING", default=False, cast=bool)
    
settings = Settings()
