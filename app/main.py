import os
from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.mount("/static", StaticFiles(directory="./static"), name="static")
templates = Jinja2Templates(directory="./templates")

exclude_pages = {"main", "base"}
available_pages = {
    os.path.splitext(f)[0]
    for f in os.listdir('./templates')
    if f.endswith('.html') and os.path.splitext(f)[0] not in exclude_pages
}

@app.get("/", include_in_schema=False)
async def main(
    request: Request,
):
    return templates.TemplateResponse(
        "main.html", {
            "request": request
        }
    )


@app.get("/{html_name}", include_in_schema=False)
async def html_home(
    html_name: str,
    request: Request,
):
    # Проверяем наличие файла
    if html_name not in available_pages:
        raise HTTPException(status_code=404, detail="Страница не найдена")
    return templates.TemplateResponse(
        f"{html_name}.html", {
            "request": request
        }
    )
