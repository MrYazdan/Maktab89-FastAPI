from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    phone: str | None = None


class Item(BaseModel):
    id: int
    name: str
    status: bool


#
# data = {
#     "id": 12,
#     # "name": '0'
# }
#
# print(User(**data))
