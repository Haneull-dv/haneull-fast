from sqlalchemy.ext.asyncio import AsyncSession
from com.haneull.account.guest.customer.model.customer_schema import CustomerSchema
from com.haneull.auth.service.retrieve_service import RetrieveService


class GetAllRepository(RetrieveService):

        async def retrieve(self, db: AsyncSession, **kwargs):
        print("💯🌈 GetAllRepository 로 진입함:")
        query = text("SELECT * FROM members")
        try:
            async with db.begin():  # 🔥 트랜잭션 자동 관리
                result = await db.execute(query)
                records = result.fetchall()
                print("💯🌈 데이터 조회 결과:", records)
                return [dict(record._mapping) for record in records]
        except SQLAlchemyError as e:
            print("⚠️ 데이터 조회 중 오류 발생:", str(e))
            await db.rollback()  # 🔥 오류 발생 시 `rollback()` 수행
            return {"error": "데이터 조회 중 오류가 발생했습니다."}

class GetListRepository(RetrieveService):
    async def retrieve(self, db: AsyncSession, retrieve_customer: CustomerSchema):
        pass