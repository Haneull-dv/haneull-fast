from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from com.haneull.account.guest.customer.models.customer_schema import CustomerSchema
from com.haneull.utils.creational.abstract.abstract_service import AbstractService
from fastapi.responses import HTMLResponse, JSONResponse
from typing import Dict, List, Any


class GetAll(AbstractService):
    async def handle(self, db: AsyncSession, **kwargs) -> List[Dict[str, Any]]:
        """
        AbstractService의 추상 메서드 구현
        """
        return await self.retrieve(db, **kwargs)
        
    async def retrieve(self, db: AsyncSession, **kwargs) -> List[Dict[str, Any]]:
        print(f"❤️❤️GetAll 로 진입함, kwargs: {kwargs}")
        try:
            # members 테이블에서 모든 데이터 조회 (비밀번호 포함)
            query = "SELECT user_id, email, name, password FROM members"
            print(f"🔍 실행할 쿼리: {query}")
            
            result = await db.fetch(query)
            print(f"📊 쿼리 결과: {result}")
            
            # JSON 형식으로 변환
            customers = []
            for record in result:
                customer_data = {
                    "user_id": record["user_id"],
                    "email": record["email"],
                    "name": record["name"],
                    "password": record["password"]
                }
                customers.append(customer_data)
                print(f"👤 고객 데이터 추가: {customer_data}")
            
            print(f"✅ 총 {len(customers)}개의 고객 데이터 반환")
            return customers
        except Exception as e:
            error_message = f"데이터 조회 중 오류가 발생했습니다: {str(e)}"
            print(f"⚠️ 경고: {error_message}")
            return {"error": error_message}
        

class GetDetail(AbstractService):
    async def handle(self, db: AsyncSession, **kwargs) -> Dict[str, Any]:
        """
        AbstractService의 추상 메서드 구현
        """
        return await self.retrieve(db, **kwargs)
        
    async def retrieve(self, db: AsyncSession, customer_id: str = None, **kwargs) -> Dict[str, Any]:
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