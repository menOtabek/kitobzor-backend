from fastapi import APIRouter

from apps.user.api_endpoints.Login import router as login_router

router = APIRouter()

router.include_router(login_router.router, prefix='/user', tags=['user'])
