import uuid
from pydantic import BaseModel, Field


class UserBase(BaseModel):
    user_name: str = Field(
        max_length=35,
        min_items=3,
        example="Timofey"
    )


class UserIn(UserBase):
    """
    Create user
    """


class UserOut(UserBase):
    id: int = Field(..., example=123)


def generate_token():
    token = str(uuid.uuid4())
    print("New token: ", token)
    return token


class User(UserOut):
    token: str = Field(default_factory=generate_token)
