from datetime import datetime
from typing import Callable
from fastapi import Depends, FastAPI
from fastapi.responses import HTMLResponse
from com.haneull.app_router import router as app_router
from com.haneull.utils.creational.singleton.db_singleton import DatabaseSingleton
from fastapi.middleware.cors import CORSMiddleware



# python -m uvicorn main:app --reload
# docker ps
# docker ps -a
# docker images
# docker start backend
# docker start database
# docker-compose
# docker exec -it database  psql -U myuser -d mydb
# docker exec -it backend bash


# python -m uvicorn fastapi.main:app --reload

app = FastAPI()

# CORS 미들웨어 설정 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # 프론트엔드 서버 주소
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드 허용
    allow_headers=["*"],  # 모든 헤더 허용
)

app.include_router(app_router)


current_time: Callable[[], str] = lambda: datetime.now(datetime.timezone('Asia/Seoul')).strftime("%Y-%m-%d %H:%M:%S")


@app.get(path="/")
async def home():
    return HTMLResponse(content=f"""                      
<body>
 <div style="width: 400px; margin: 50 auto;">
    <h1> 현재 서버 구동 중입니다.</h1>   
 </div>
</body>
 """)


