from sqlalchemy.orm import Session
from com.haneull.account.guest.customer.model.customer_schema import CustomerSchema
from com.haneull.auth.service.create_service import CreateService


class DefaultCreateRepository(CreateService):
        
    def create(self, db: Session, new_customer: CustomerSchema):
        print("😶‍🌫️❤️👻Repository new_customer 정보", new_customer)

class ValidatedCreateRepository(CreateService):
    def create(self, db: Session, new_customer: CustomerSchema):
        pass


