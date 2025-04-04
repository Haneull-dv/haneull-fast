from fastapi import APIRouter
from com.haneull.account.guest.customer.api.customer_router import router as customer_router
from com.haneull.account.staff.manager.web.manager_router import router as manager_router

account_router = APIRouter()

account_router.include_router(customer_router, prefix="/customer")
account_router.include_router(manager_router, prefix="/manager")