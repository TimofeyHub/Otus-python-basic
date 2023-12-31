import uvicorn
from fastapi import FastAPI

from view import router as homework_03_router, prefix as homework_03_prefix
from items.items_views import router as items_router, prefix as item_prefix
from users.views import router as users_router, prefix as users_prefix

app = FastAPI()
app.include_router(items_router, prefix=item_prefix)
app.include_router(users_router, prefix=users_prefix)
app.include_router(homework_03_router, prefix=homework_03_prefix)


@app.get("/")
def health_check():
    return {"message": "Hello!"}


@app.get("/hello/")
def hello(name: str = "World"):
    return {"message": f"Hello, {name}!"}


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
