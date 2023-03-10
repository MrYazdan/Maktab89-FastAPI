from fastapi import FastAPI, Cookie, Request
from auth.db import users_db
from auth.schemas import UserPublicSchema
from auth.router import auth_router
from auth.utils import get_user_by_token
from uuid import UUID


app = FastAPI()


@app.middleware("http")
async def user_middleware(request: Request, view):
    if token := request.cookies.get("token", None):
        user = get_user_by_token(token)
        request.scope.update({"user_logged_in": user})
    # print("before called view")
    response = await view(request)
    # print(response.__dict__)
    # print("after called view")

    return response


@app.get("/")
# async def root(request: Request):
async def root(token: UUID | None = Cookie(default=None)):
    res = {"message": "Hello World"}
    # if settings.user_login:
    #     res.update({"user": settings.user_login.username})
    # if username := request.cookies.get("username", None):
    if token:
        for user in users_db:
            if user.token == token:
                res.update({"login_user": UserPublicSchema(**user.dict())})

    return res


app.include_router(router=auth_router, prefix="/auth")
