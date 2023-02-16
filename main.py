from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from schemas import Item

app = FastAPI()
TEMPLATE = Jinja2Templates(directory="templates")

items = [
    {"id": 1, "name": "python", "status": True},
    {"id": 2, "name": "js", "status": True},
    {"id": 3, "name": "django", "status": True},
    {"id": 4, "name": "express", "status": True},
    {"id": 5, "name": "fastApi", "status": True},
    {"id": 6, "name": "flask", "status": True},
    {"id": 7, "name": "vue", "status": True},
]

for item in items:
    _item = items.pop(0)
    items.append(Item(**_item))


@app.get("/hi/")
@app.get("/hi/{name}")
async def hi(name: str = "Yazdan"):
    return {"detail": f"hi {name}"}


@app.get("/math/{number_one}/power/")
@app.get("/math/{number_one}/power/{number_two}")
async def hi(number_one: int, number_two: int = 2) -> dict:
    return {
        "detail": {
            "type": "power",
            "data": [
                {
                    "name": "number_one",
                    "value": number_one,
                    "type": str(type(number_one))
                },
                {
                    "name": "number_two",
                    "value": number_two,
                    "type": str(type(number_two))
                }
            ],
            "value": number_one ** number_two
        }
    }


@app.get("/items/{item_id}")
async def get_item(item_id: int) -> dict:
    return {"items": [item for item in items if item.id == item_id]}


@app.get("/")
def home(request: Request):
    return TEMPLATE.TemplateResponse(
        "home.html",
        {"request": request, "products": items}
    )


@app.post("/")
def home(request: Request, id: int = Form(), name: str = Form(), status: bool = Form(default=False)):
    items.append(Item(id=id, name=name, status=status))
    return TEMPLATE.TemplateResponse(
        "home.html",
        {"request": request, "products": items}
    )
