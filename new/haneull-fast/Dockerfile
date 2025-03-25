FROM python:3.11-slim

# 1. 작업 디렉토리 지정
WORKDIR /app

# 2. requirements.txt 복사 및 설치
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 3. 전체 앱 복사
COPY . .

# 4. FastAPI 실행
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
