from fastapi import APIRouter, HTTPException, status

from . import crud
from .schemas import UserIn, UserOut

router = APIRouter(tags=["Users"])
prefix = "/users"


@router.get("/", response_model=list[UserOut])
def get_users() -> list[UserOut]:
    return crud.get_users_list()


@router.post("/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def create_user(user_in: UserIn) -> UserOut:
    return crud.create_user(user_in=user_in)


@router.get("/{user_id}/", response_model=UserOut)
def get_user_by_id(user_id: int) -> UserOut:
    user = crud.get_user_by_id(user_id=user_id)
    if user:
        return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User #{user_id} not found!"
    )
