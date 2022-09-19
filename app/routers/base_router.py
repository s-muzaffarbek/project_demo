from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from settings import templates

router = APIRouter(
    prefix="/blog",
    tags=['blog']
)

@router.get("/", response_class=HTMLResponse)
async def blog_home(request: Request):
    context = {
        'request': request,
    }
    return templates.TemplateResponse('blog/blog_list.html', context)

@router.get("/edit", response_class=HTMLResponse)
async def blog_edit(request: Request):
    context = {
        'request': request,
    }
    return templates.TemplateResponse('edit.html', context)

@router.get(f"/edit/{blog_id}", response_class=HTMLResponse)
async def blog_edit_id(request: Request, blog_id: int):
    context = {
        'request': request,
        'blog': blog_id,
    }
    return templates.TemplateResponse('blog_edit.html', context)