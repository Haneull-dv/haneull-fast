from com.haneull.account.guest.customer.storage.get_customer import GetAllRepository, GetDetailRepository
from sqlalchemy.ext.asyncio import AsyncSession

from com.haneull.utils.creational.abstract.abstract_service import AbstractService

class GetAll(AbstractService):
    async def handle(self, db: AsyncSession, **kwargs):
        repository = GetAllRepository()
        return await repository.retrieve(db, **kwargs)

class GetDetail(AbstractService):
    async def handle(self, db: AsyncSession, **kwargs):
        user_id = kwargs.get('user_id')
        repository = GetDetailRepository()
        return await repository.retrieve(db, user_id)
