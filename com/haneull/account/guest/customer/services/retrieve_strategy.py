from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from com.haneull.account.guest.customer.models.customer_schema import CustomerSchema
from com.haneull.utils.creational.abstract.abstract_service import AbstractService
from fastapi.responses import HTMLResponse, JSONResponse


class GetAll(AbstractService):
    def handle(self, db: AsyncSession, **kwargs):
        """
        AbstractService의 추상 메서드 구현
        """
        return self.retrieve(db, **kwargs)
        
    async def retrieve(self, db: AsyncSession, **kwargs):
        try:
            # members 테이블에서 모든 데이터 조회 (비밀번호 포함)
            query = "SELECT user_id, email, name, password FROM members"
            result = await db.fetch(query)
            
            # JSON 형식으로 변환
            customers = []
            for record in result:
                customers.append({
                    "user_id": record["user_id"],
                    "email": record["email"],
                    "name": record["name"],
                    "password": record["password"]
                })
            
            return customers
        except Exception as e:
            error_message = f"데이터 조회 중 오류가 발생했습니다: {str(e)}"
            print(f"⚠️ 경고: {error_message}")
            return {"error": error_message}
        

class GetDetail(AbstractService):
    def handle(self, db: AsyncSession, **kwargs):
        """
        AbstractService의 추상 메서드 구현
        """
        return self.retrieve(db, **kwargs)
        
    async def retrieve(self, db: AsyncSession, customer_id: str = None, **kwargs):
        if not customer_id:
            raise ValueError("고객 ID가 제공되지 않았습니다.")
        
        try:
            # 특정 고객 조회 (비밀번호 포함)
            query = f"SELECT user_id, email, name, password FROM members WHERE user_id = '{customer_id}'"
            result = await db.fetch(query)
            
            if not result:
                return {"error": f"고객 ID {customer_id}에 해당하는 정보를 찾을 수 없습니다."}
            
            customer = result[0]
            
            return {
                "user_id": customer["user_id"],
                "email": customer["email"],
                "name": customer["name"],
                "password": customer["password"]
            }
        except Exception as e:
            error_message = f"고객 정보 조회 중 오류가 발생했습니다: {str(e)}"
            print(f"⚠️ 경고: {error_message}")
            return {"error": error_message}