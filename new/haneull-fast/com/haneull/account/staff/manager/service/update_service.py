from abc import ABC, abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession
from com.haneull.account.staff.manager.model.manager_schema import ManagerSchema


class UpdateService(ABC):

    @abstractmethod
    async def update(self, db: AsyncSession, update_customer: ManagerSchema):
        pass
