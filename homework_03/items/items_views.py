from fastapi import APIRouter

ITEMS_LIST = [
    {"id": 1, "name": "book"},
    {"id": 2, "name": "toy"},
    {"id": 3, "name": "tv"},
]

router = APIRouter(tags=["Items"])
prefix = "/items"


@router.get("/")
def get_items():
    return ITEMS_LIST


@router.post("/")
def create_item(data: dict[str, str]):
    return data


@router.get("/{item_id}/")
def get_item_by_id(item_id: int):
    for item in ITEMS_LIST:
        if item_id == item.get("id"):
            return item
