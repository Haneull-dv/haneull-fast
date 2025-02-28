from datetime import datetime
from typing import Callable
from fastapi import FastAPI
from pytz import timezone
from fastapi.responses import HTMLResponse
from com.config.database import SessionLocal
from com.haneull.auth.user.web import router as user_router
from com.haneull.auth.admin.web import router as admin_router
from com.haneull.auth.stock.web import router as stock_router
# python -m uvicorn fastapi.main:app --reload

app = FastAPI()

app.include_router(user_router, prefix="/user", tags=["User"])
app.include_router(admin_router, prefix="/admin", tags=["Admin"])
app.include_router(stock_router, prefix="/stock", tags=["Admin"])
current_time: Callable[[], str] = lambda: datetime.now(datetime.timezone('Asia/Seoul')).strftime("%Y-%m-%d %H:%M:%S")

@app.get("/")
async def hello_world():
    return {"message": "Hello World!"}


@app.get(path="/")
async def home():
    return HTMLResponse(content=f"""
                        
<body>
 <div style="width: 400px; margin: 50 auto;">
    <h1> 현재 서버 구동 중입니다.</h1>
#     <h2>{current_time()}</h2>
 </div>
</body>
 """)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "FastAPI + Docker + PostgreSQL 연결 성공!"}