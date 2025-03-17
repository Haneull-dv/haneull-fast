from abc import ABC, abstracmethod
from sqlalchemy.orm import Session

class RetrieveService(ABC):

    @abstracmethod
    def retrieve(self, db: Session, **kwargs):
        pass