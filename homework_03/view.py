from fastapi import APIRouter, status

router = APIRouter(tags=["homework_03"])
prefix = "/ping"


@router.get("/", status_code=status.HTTP_200_OK)
def get_ping():
    return {"message": "pong"}
