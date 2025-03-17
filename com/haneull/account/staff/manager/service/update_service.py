from abc import ABC, abstracmethod
from sqlalchemy.orm import Session
from com.haneull.account.guest.customer.model.customer_schema import CustomerSchema

class UpdateService(ABC):

    @abstracmethod
    def update(self, db: Session, update_customer: CustomerSchema):
        pass