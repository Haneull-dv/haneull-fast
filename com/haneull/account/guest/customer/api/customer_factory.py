from typing import Literal
from sqlalchemy.ext.asyncio import AsyncSession
from com.haneull.account.guest.customer.services.create_custmer_service import CreateCustomer
from com.haneull.account.guest.customer.services.delete_customer_service import DeleteCustomer
from com.haneull.account.guest.customer.services.retrieve_customer_service import GetAll, GetDetail
from com.haneull.account.guest.customer.models.customer_action import CustomerAction
from com.haneull.account.guest.customer.services.update_customer_service import UpdateCustomer


class CustomerFactory:

    _strategy_map = {
        CustomerAction.CREATE_CUSTOMER: CreateCustomer(),
        CustomerAction.GET_ALL: GetAll(),
        CustomerAction.GET_DETAIL: GetDetail(),
        CustomerAction.FULL_UPDATE: UpdateCustomer(),
        CustomerAction.DELETE_CUSTOMER: DeleteCustomer()
    }

    @staticmethod
    async def execute(strategy, **kwargs):
        print("👻👻execute 로 진입함", kwargs)
        instance = CustomerFactory._strategy_map[strategy]
        if not instance:
            raise Exception("invalid strategy")
        return await instance.handle(**kwargs)