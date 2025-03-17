from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from com.haneull.account.guest.customer.models.customer_schema import CustomerSchema
from com.haneull.auth.service.create_service import CreateService
from com.haneull.utils.creational.abstract.abstract_service import AbstractService


class CreateCustomer(AbstractService):
    def handle(self, db: AsyncSession, **kwargs):
        """
        AbstractService의 추상 메서드 구현
        """
        return self.create(db, **kwargs)
        
    def create(self, db: Session, new_customer: CustomerSchema):
        customer_repo = CreateService(db)
        return customer_repo.create(new_customer)
       

