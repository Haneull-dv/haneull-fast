from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from com.haneull.account.guest.customer.models.customer_schema import CustomerSchema
from com.haneull.auth.service.delete_service import DeleteService
from com.haneull.utils.creational.abstract.abstract_service import AbstractService


class DeleteCustomer(AbstractService):
    def handle(self, db: AsyncSession, **kwargs):
        """
        AbstractService의 추상 메서드 구현
        """
        return self.delete(db, **kwargs)
        
    async def delete(self, db: AsyncSession, customer_id: str = None, **kwargs):
        if not customer_id:
            raise ValueError("고객 ID가 제공되지 않았습니다.")
        
        # 여기에 삭제 로직 구현
        return {"message": f"고객 ID {customer_id}에 대한 삭제 기능은 아직 구현되지 않았습니다."}

