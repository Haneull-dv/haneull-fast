from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from com.haneull.account.common.user.model.user_schema import MemberResponse, MemberCreate
from com.haneull.utils.creational.builder.db_builder import get_db

router = APIRouter()

@router.get("/list", response_model=List[MemberResponse])
async def get_members_list(db: AsyncSession = Depends(get_db)):
    """
    members 테이블의 모든 회원 목록을 조회합니다.
    """
    try:
        # members 테이블에서 모든 데이터 조회
        query = "SELECT user_id, email, name, password FROM members"
        result = await db.fetch(query)
        
        # 결과가 없는 경우
        if not result:
            return []
        
        # JSON 형식으로 변환
        members = []
        for record in result:
            members.append({
                "user_id": record["user_id"],
                "email": record["email"],
                "name": record["name"],
                "password": record["password"]
            })
        
        return members
    except Exception as e:
        error_message = f"회원 목록 조회 중 오류가 발생했습니다: {str(e)}"
        print(f"⚠️ 경고: {error_message}")
        raise HTTPException(status_code=500, detail=error_message)

@router.post("/signup", response_model=MemberResponse)
async def create_member(member: MemberCreate, db: AsyncSession = Depends(get_db)):
    """
    새로운 회원을 등록합니다.
    """
    try:
        # 이미 존재하는 사용자 ID 확인
        check_query = f"SELECT user_id FROM members WHERE user_id = '{member.user_id}'"
        check_result = await db.fetch(check_query)
        
        if check_result:
            raise HTTPException(status_code=400, detail="이미 존재하는 사용자 ID입니다.")
        
        # 이미 존재하는 이메일 확인
        check_email_query = f"SELECT email FROM members WHERE email = '{member.email}'"
        check_email_result = await db.fetch(check_email_query)
        
        if check_email_result:
            raise HTTPException(status_code=400, detail="이미 존재하는 이메일입니다.")
        
        # 새 회원 등록
        insert_query = f"""
        INSERT INTO members (user_id, email, name, password)
        VALUES ('{member.user_id}', '{member.email}', '{member.name}', '{member.password}')
        RETURNING user_id, email, name, password
        """
        
        result = await db.fetch(insert_query)
        await db.execute("COMMIT")
        
        if not result:
            raise HTTPException(status_code=500, detail="회원 등록에 실패했습니다.")
        
        created_member = result[0]
        
        return {
            "user_id": created_member["user_id"],
            "email": created_member["email"],
            "name": created_member["name"],
            "password": created_member["password"]
        }
    except HTTPException:
        raise
    except Exception as e:
        error_message = f"회원 등록 중 오류가 발생했습니다: {str(e)}"
        print(f"⚠️ 경고: {error_message}")
        raise HTTPException(status_code=500, detail=error_message) 