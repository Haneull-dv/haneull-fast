from fastapi import APIRouter
from com.haneull.account.account_router import account_router
from com.haneull.auth.auth_router import auth_router

router = APIRouter()

router.include_router(account_router, prefix="/account")
router.include_router(auth_router, prefix="/auth")
