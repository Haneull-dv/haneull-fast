from fastapi import APIRouter



router = APIRouter()

@router.get("/")
def hello():
    return stock_service.hello()
@router.get("/add")
def add_user(user):
    print(f":두꺼운_더하기_기호:컨트롤러 사용자 추가: {user}")
    return UserService().add_user()
@router.get("/get")
def get_user(user):
    print(f":컴퓨터:컨트롤러 사용자 조회: {user}")
    return UserService().get_user()
@router.get("/update")
def update_user(user):
    print(f":구름_속의_얼굴:컨트롤러 사용자 수정: {user}")
    return UserService().update_user()
@router.get("/delete")
def delete_user(user):
    print(f":호박등:컨트롤러 사용자 삭제: {user}")
    return UserService().delete_user()


