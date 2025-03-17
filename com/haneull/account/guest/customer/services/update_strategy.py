from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from com.haneull.account.guest.customer.models.customer_schema import CustomerSchema
from com.haneull.utils.creational.abstract.abstract_service import AbstractService



class UpdateCustomer(AbstractService):
    def handle(self, db: AsyncSession, **kwargs):
        """
        AbstractService의 추상 메서드 구현
        """
        return self.update(db, **kwargs)
        
    def update(self, db: Session, update_customer: CustomerSchema):
        pass

