from fastapi import APIRouter
from auth.routes.users import router as users_router

auth_router = APIRouter()

auth_router.include_router(users_router)
