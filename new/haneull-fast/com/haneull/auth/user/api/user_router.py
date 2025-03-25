from fastapi import APIRouter, Depends, Body
from sqlalchemy.ext.asyncio import AsyncSession
from com.haneull.account.common.user.model.user_schema import UserSchema
from com.haneull.auth.user.services.user_lookup import UserLookupService
from com.haneull.utils.creational.builder.db_builder import get_db
from com.haneull.auth.user.models.login_schema import LoginRequest, LoginResponse

router = APIRouter()

@router.post("/login", response_model=LoginResponse)
async def login(
    login_data: LoginRequest,
    db: AsyncSession = Depends(get_db)
):
    print(f"로그인 요청 - ID: {login_data.user_id}")  # 비밀번호는 로그에 출력하지 않음
    service = UserLookupService(db)
    return await service.login(login_data.user_id, login_data.password)

