from fastapi import APIRouter
from com.haneull.account.guest.customer.api.customer_router import router as customer_router
from com.haneull.account.common.user.api.member_router import router as member_router


router = APIRouter()
router.include_router(customer_router, prefix="/customer")
router.include_router(member_router, prefix="/members")