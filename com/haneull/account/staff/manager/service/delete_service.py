from abc import ABC, abstracmethod
from sqlalchemy.orm import Session

class DeleteService(ABC):

    @abstracmethod
    def delete(self, db: Session, user_id: str):
        pass