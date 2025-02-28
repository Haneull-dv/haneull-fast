from fastapi import APIRouter
from com.haneull.auth.user.service.get_all_users import UserService
from com.haneull.auth.user.web import user_controller


router = APIRouter()
controller = user_controller()

@router.get(path="/")

async def hello_user():
    return controller.hello_user()

@router.get(path="/")
async def hello_user():
    return controller.hello_user()
