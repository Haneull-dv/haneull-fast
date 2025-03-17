from sqlalchemy.ext.asyncio import AsyncSession
from com.haneull.account.guest.customer.model.customer_schema import CustomerSchema
from com.haneull.auth.service.delete_service import DeleteService


class SoftDeleteRepository(DeleteService):
        
    async def delete(self, db: AsyncSession, delete_customer: CustomerSchema):
        pass

class HardDeleteRepository(DeleteService):
    async def delete(self, db: AsyncSession, delete_customer: CustomerSchema):
        pass