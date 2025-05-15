from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# 1) Подключаем папку static под URL /static
app.mount("/static", StaticFiles(directory="../static"), name="static")

# 2) Настраиваем Jinja2-шаблоны из папки templates
templates = Jinja2Templates(directory="../templates")


@app.get("/react", include_in_schema=False)
async def react_home(request: Request):
    return templates.TemplateResponse(
        "react.html", {
            "request": request
        }
    )
