from sqlalchemy.orm import Session
from com.haneull.account.guest.customer.model.customer_schema import CustomerSchema
from com.haneull.auth.service.update_service import UpdateService



class FullUpdateStrategy(UpdateService):
        
    def update(self, db: Session, update_customer: CustomerSchema):
        pass

class PartialUpdateStrategy(UpdateService):
    def update(self, db: Session, update_customer: CustomerSchema):
        pass