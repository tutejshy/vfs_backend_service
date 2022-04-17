from fastapi import FastAPI
from app.api.v1 import api

from app.core.settings import get_settings, Settings
from starlette.middleware.cors import CORSMiddleware


def create_application(settings: Settings) -> FastAPI:

    apps = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.PROJECT_VERSION,
        openapi_url=settings.openapi_url()
    )

    apps.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_origins=settings.allow_origins(),
        allow_methods=["*"],
        allow_headers=["*"],
    )

    apps.include_router(api.router, prefix=settings.API_V1_PATH)

    return apps


app = create_application(get_settings())
