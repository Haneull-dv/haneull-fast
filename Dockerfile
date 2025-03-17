# Python 3.12 기반 이미지 사용
FROM python:3.12.7-slim

# 작업 디렉토리 설정
WORKDIR /backend

# 의존성 파일 복사 및 설치
COPY requirements.txt /backend/
RUN pip install -r /backend/requirements.txt

# FastAPI 애플리케이션 코드 복사
COPY . /backend/

# FastAPI 실행
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
