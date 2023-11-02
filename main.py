from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def get_root():
    return {"msg": "root"}

@app.get("/items", response_class=HTMLResponse)
def get_items(request: Request):
    items = ["Item 1", "Item 2"]
    return templates.TemplateResponse("items.html", {"request": request, "items": items})

@app.get("/error")
def get_error():
    raise HTTPException(status_code=404, detail="Item not found")

@app.get("/notimplemented")
def get_not_implemented():
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED
    )
