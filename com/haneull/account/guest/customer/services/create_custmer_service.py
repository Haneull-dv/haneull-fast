from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from com.haneull.account.guest.customer.models.customer_schema import CustomerSchema
from com.haneull.utils.creational.abstract.abstract_service import AbstractService
from typing import Dict, Any


class CreateCustomer(AbstractService):
    async def handle(self, db: AsyncSession, **kwargs) -> Dict[str, Any]:
        """
        AbstractService의 추상 메서드 구현
        """
        # 필요없는 'method' 키워드 인자 제거
        if 'method' in kwargs:
            kwargs.pop('method')
        
        # create_customer 키가 있으면 customer로 이름 변경
        if 'create_customer' in kwargs:
            kwargs['customer'] = kwargs.pop('create_customer')
            
        return await self.create(db, **kwargs)
        
    async def create(self, db: AsyncSession, customer: CustomerSchema = None, **kwargs) -> Dict[str, Any]:
        print(f"💡💡 create 메서드 진입, customer: {customer}, kwargs: {kwargs}")
        if not customer:
            print("❌❌ 고객 정보가 없습니다!")
            return {"error": "고객 정보가 제공되지 않았습니다."}
        
        try:
            # 고객 생성 쿼리 실행
            query = f"""
            INSERT INTO members (user_id, email, name, password)
            VALUES ('{customer.user_id}', '{customer.email}', '{customer.name}', '{customer.password}')
            RETURNING user_id, email, name, password
            """
            print(f"🔍🔍 실행할 쿼리: {query}")
            
            result = await db.fetch(query)
            print(f"📊📊 쿼리 실행 결과: {result}")
            await db.execute("COMMIT")
            
            if not result:
                print("❌❌ 쿼리 결과가 없습니다!")
                return {"error": "고객 생성에 실패했습니다."}
            
            created_customer = result[0]
            print(f"✅✅ 고객 생성 성공: {created_customer}")
            
            return {
                "user_id": created_customer["user_id"],
                "email": created_customer["email"],
                "name": created_customer["name"],
                "password": created_customer["password"]
            }
        except SQLAlchemyError as e:
            await db.execute("ROLLBACK")
            error_message = f"고객 생성 중 오류가 발생했습니다: {str(e)}"
            print(f"⚠️ 경고: {error_message}")
            return {"error": error_message}
       

