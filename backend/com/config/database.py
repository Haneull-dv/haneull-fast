from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# 1️⃣ 환경 변수에서 DATABASE_URL 가져오기 (docker-compose.yml에서 설정한 값)
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://myuser:mypassword@localhost:5432/mydatabase")

# 2️⃣ 데이터베이스 엔진 생성 (PostgreSQL 연결)
engine = create_engine(DATABASE_URL)

# 3️⃣ 세션 설정 (데이터베이스 트랜잭션 관리)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4️⃣ Base 클래스 생성 (모델 정의 시 사용)
Base = declarative_base()
