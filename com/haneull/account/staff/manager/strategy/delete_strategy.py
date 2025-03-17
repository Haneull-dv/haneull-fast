from sqlalchemy.orm import Session
from com.haneull.account.guest.customer.model.customer_schema import CustomerSchema
from com.haneull.auth.service.delete_service import DeleteService


class SoftDeleteStrategy(DeleteService):
        
    def delete(self, db: Session, delete_customer: CustomerSchema):
        pass

class HardDeleteStrategy(DeleteService):
    def delete(self, db: Session, delete_customer: CustomerSchema):
        pass