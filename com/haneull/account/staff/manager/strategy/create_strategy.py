from sqlalchemy.orm import Session
from com.haneull.account.staff.manager.model.manager_schema import ManagerSchema
from com.haneull.auth.service.create_service import CreateService


class DefaultCreateRepository(CreateService):       
    def create(self, db: Session, new_manager: ManagerSchema):
        manager_repo = DefaultCreateRepository(db)
        return manager_repo.create(new_manager)
       
class ValidatedCreateRepository(CreateService):
    def create(self, db: Session, new_manager: ManagerSchema):
        pass
