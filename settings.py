from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount('/static', StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
def read_item(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

