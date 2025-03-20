from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from com.haneull.account.guest.customer.models.customer_schema import CustomerSchema
from com.haneull.utils.creational.abstract.abstract_service import AbstractService
from typing import Dict, Any


class UpdateCustomer(AbstractService):
    async def handle(self, db: AsyncSession, **kwargs) -> Dict[str, Any]:
        """
        AbstractService의 추상 메서드 구현
        """
        return self.update(db, **kwargs)
        
    async def update(self, db: AsyncSession, update_customer: CustomerSchema):
        pass

