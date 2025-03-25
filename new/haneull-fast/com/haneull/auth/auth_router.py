from fastapi import APIRouter

from com.haneull.auth.user.api import router as user_router


auth_router = APIRouter()

auth_router.include_router(user_router, prefix="/user")
