from sqlalchemy.ext.asyncio import AsyncSession
from com.haneull.account.guest.customer.model.customer_entity import CustomerEntity
from com.haneull.account.guest.customer.model.customer_schema import CustomerSchema
from com.haneull.auth.service.create_service import CreateService


class DefaultCreateRepository(CreateService):
        
   async def create(self, db: AsyncSession, new_customer: CustomerSchema):
        print("😶‍🌫️❤️👻Repository new_customer 정보", new_customer)
        db.add(CustomerEntity(
            user_id = new_customer.user_id,
            name = new_customer.name,
            email = new_customer.email,
            password = new_customer.password
        ))
        db.commit()
        db.refresh(new_customer)
        return new_customer

class ValidatedCreateRepository(CreateService):
    async def create(self, db: AsyncSession, new_customer: CustomerSchema):
        pass


