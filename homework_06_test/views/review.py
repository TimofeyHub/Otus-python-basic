from flask import Blueprint, render_template

review_app = Blueprint(
    "review_app",
    __name__,
    url_prefix='/review'
)


@review_app.get("/", endpoint="list")
def get_review_list():
    pass


@review_app.post("/add/", endpoint="add")
def add_review():
    pass
