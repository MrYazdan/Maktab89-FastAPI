from uuid import UUID
from auth.db import users_db

from auth.schemas import UserPublicSchema


def get_user_by_token(token: str | UUID) -> UserPublicSchema | None:
    for user in users_db:
        if str(user.token) == token:
            return UserPublicSchema(**user.dict())
    return None
