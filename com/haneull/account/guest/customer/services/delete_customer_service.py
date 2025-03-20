from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from com.haneull.account.guest.customer.models.customer_schema import CustomerSchema
from com.haneull.utils.creational.abstract.abstract_service import AbstractService
from typing import Dict, Any


class DeleteCustomer(AbstractService):
    async def handle(self, db: AsyncSession, **kwargs) -> Dict[str, Any]:
        """
        AbstractService의 추상 메서드 구현
        """
        return self.delete(db, **kwargs)
        
    async def delete(self, db: AsyncSession, customer_id: str = None, **kwargs):
        if not customer_id:
            raise ValueError("고객 ID가 제공되지 않았습니다.")
        
        # 여기에 삭제 로직 구현
        return {"message": f"고객 ID {customer_id}에 대한 삭제 기능은 아직 구현되지 않았습니다."}

