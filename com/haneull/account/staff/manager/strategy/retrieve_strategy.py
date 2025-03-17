from sqlalchemy.orm import Session
from com.haneull.account.guest.customer.model.customer_schema import CustomerSchema
from com.haneull.auth.service.retrieve_service import RetrieveService



class GetAllStrategy(RetrieveService):
        
    def retrieve(self, db: Session, retrieve_customer: CustomerSchema):
        pass

class GetListStrategy(RetrieveService):
    def retrieve(self, db: Session, retrieve_customer: CustomerSchema):
        pass