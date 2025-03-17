from sqlalchemy.ext.asyncio import AsyncSession
from com.haneull.account.guest.customer.model.customer_schema import CustomerSchema
from com.haneull.auth.service.update_service import UpdateService

class FullUpdateRepository(UpdateService):
        
    async def update(self, db: AsyncSession, update_customer: CustomerSchema):
        pass

class PartialUpdateRepository(UpdateService):
    async def update(self, db: AsyncSession, update_customer: CustomerSchema):
        pass