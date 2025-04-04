from sqlalchemy.ext.asyncio import AsyncSession
from com.haneull.account.staff.manager.service.delete_service import DeleteService


class SoftDeleteRepository(DeleteService):
    async def delete(self, db: AsyncSession, user_id: str):
        pass
class HardDeleteRepository(DeleteService):
    async def delete(self, db: AsyncSession, user_id: str):
        pass
