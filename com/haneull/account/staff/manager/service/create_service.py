from abc import ABC, abstracmethod
from sqlalchemy.orm import Session
from com.haneull.account.guest.customer.model.customer_schema import CustomerSchema

class CreateService(ABC):

    @abstracmethod
    def execute(self, db: Session, new_customer: CustomerSchema):
        pass