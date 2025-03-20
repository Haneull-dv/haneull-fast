from sqlalchemy import Column, Integer, String
from database import Base

# SQLAlchemy ORM 모델 (members 테이블 매핑)
class Member(Base):
    __tablename__ = "members"

    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String(20), unique=True, nullable=True)
    password = Column(String(20), nullable=False)
    name = Column(String(10), unique=True, nullable=False)
