from fastapi import APIRouter

from app.api.v1.routes import demo_route

router = APIRouter()
router.include_router(demo_route.router, prefix="/demo", tags=["demo"])
