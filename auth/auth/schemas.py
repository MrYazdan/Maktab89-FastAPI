from pydantic import BaseModel, Field
from uuid import uuid4, UUID


class UserPublicSchema(BaseModel):
    id: int = 0
    username: str
    full_name: str | None = None
    age: int | None = None


class UserPrivateSchema(UserPublicSchema):
    password: str
    token: UUID = Field(default_factory=uuid4)
