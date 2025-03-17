from fastapi import APIRouter


router = APIRouter()
controller = article_controller()

@router.post(path="/article/create")
async def create_article():
    return controller.hello_article()

@router.get(path="/article/detail")
async def get_article_detail():
    return controller.hello_article()

@router.get("/article/list")
    pass
    
@router.put(path="/article/update")
pass
    return controller.hello_article()

@router.delete(path="/article/delete")
async def delete_article():
    return controller.hello_article()