from typing import Any, Optional

from fastapi import Depends, APIRouter, Request

from app.api.deps import deps
from app.utils.util import json_of

router = APIRouter()


@router.get("/master/center/{to}/blr")
async def centers(to: str, request: Request = Depends(deps.request_debug)) -> Optional[Any]:
    return json_of(f'data/v1/{to}_centers.json')


@router.get("/master/visacategory/{to}/blr/{center_code}")
async def categories(to: str, center_code: str, request: Request = Depends(deps.request_debug)) -> Optional[Any]:
    return json_of(f'data/v1/{to}_{center_code}_categories.json')


@router.get("/master/subvisacategory/{to}/blr/{center_code}/{parent_code}")
async def children_categories(to: str, center_code: str, parent_code: str, request: Request = Depends(deps.request_debug)) -> Optional[Any]:
    return json_of(f'data/v1/{to}_{center_code}_categories_{parent_code}.json')


@router.get("/appointment/slots")
async def slots(missionCode: str, request: Request = Depends(deps.request_debug)) -> Optional[Any]:
    return json_of(f'data/v1/{missionCode}_slots.json')


@router.post("/user/login")
async def login(request: Request = Depends(deps.request_debug)) -> Any:
    return json_of('data/v1/login.json')
