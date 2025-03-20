from fastapi import APIRouter, Depends
from sqlalchemy import select, text
from sqlalchemy.ext.asyncio import AsyncSession
from com.haneull.account.guest.customer.models.customer_entity import CustomerEntity
from com.haneull.account.guest.customer.models.customer_schema import CustomerSchema
from com.haneull.account.guest.customer.api.customer_controller import CustomerController
from com.haneull.utils.creational.builder.db_builder import get_db
import asyncpg
from fastapi.responses import HTMLResponse
from typing import List, Dict, Any


router = APIRouter()
controller = CustomerController()

@router.post(path="/create")
async def create_customer(create_customer: CustomerSchema, db: AsyncSession = Depends(get_db)):
    print("👮👮 customer router create_customer 진입함", create_customer)
    return await controller.create_customer(db=db, create_customer=create_customer)

@router.get(path="/detail")
async def get_customer_detail(customer_id: str, db: AsyncSession = Depends(get_db)):
    return await controller.get_customer_detail(db=db, customer_id=customer_id)

@router.get("/list", response_model=List[Dict[str, Any]])
async def get_customer_list(db: AsyncSession = Depends(get_db)):
    print("🎉🎉 customer router get_customer_list 진입함")
    return await controller.get_customer_list(db=db)

@router.put(path="/update")
async def update_customer(update_customer: CustomerSchema, db: AsyncSession = Depends(get_db)):
    return await controller.update_customer(db=db, update_customer=update_customer)

@router.delete(path="/delete")
async def delete_customer(user_id: str, db: AsyncSession = Depends(get_db)):
    return await controller.delete_customer(db=db, user_id=user_id)