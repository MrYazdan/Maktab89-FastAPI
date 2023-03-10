from fastapi import APIRouter, FastAPI
from fastapi import HTTPException, status, Request, Response
from fastapi.templating import Jinja2Templates
from auth.schemas import UserPublicSchema, UserPrivateSchema
from auth.db import users_db

router = APIRouter()
template = Jinja2Templates(directory="templates/auth")


@router.get("/login")
def login(request: Request):
    return template.TemplateResponse(
        "login.html",
        {"request": request}
    )


@router.get("/logout")
def logout(response: Response):
    response.delete_cookie("token")
    # settings.user_login = None
    return {"status": "Logout successful"}


# @app.post("/login")
# async def login(request: Request):
#     data = await request.body()
#     from json import loads
#     data = loads(data)
#
#     print(data)
@router.post("/login", response_model=UserPublicSchema)
def login(user_instance: UserPrivateSchema, response: Response):
    for user in users_db:
        if user.username == user_instance.username and user.password == user_instance.password:
            # http_only => xss | document.cookie
            # secure => ssl | https
            # ----
            # accept_token
            # refresh_token
            response.set_cookie("token", str(user.token), max_age=6000, httponly=True, secure=True)
            return user

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password"
    )
