from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from settings import templates

router = APIRouter(
    prefix="/user",
    tags=['user']
)

@router.get("/user", response_class=HTMLResponse)
async def user_home(request: Request):
    context = {
        'request': request,
    }
    return templates.TemplateResponse('account/user_detail.html', context)