from functools import lru_cache
from typing import List, Union
from pydantic import BaseSettings, validator


class Settings(BaseSettings):
    API_V1_PATH: str = "/api/v1"

    # Project
    PROJECT_NAME: str
    PROJECT_VERSION: str

    def openapi_url(self) -> str:
        return f'{self.API_V1_PATH}/openapi.json'

    def allow_origins(self) -> List[str]:
        return self.BACKEND_CORS_ORIGINS if self.BACKEND_CORS_ORIGINS else ['*']

    # CORS
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:8080"]'
    BACKEND_CORS_ORIGINS: List[str] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    return Settings()
