from pydantic import BaseModel

from .schemas import User, UserIn


class Storage(BaseModel):
    users: dict[int, User] = {}
    last_id: int = 0

    @property
    def next_id(self):
        self.last_id += 1
        return self.last_id

    def create_user(self, user_name: str) -> User:
        user = User(id=self.next_id, user_name=user_name)
        self.users[user.id] = user
        return user


storage = Storage()

storage.create_user("Tim")
storage.create_user("Sam")
storage.create_user("Kamui")


def get_users_list() -> list[User]:
    return list(storage.users.values())


def create_user(user_in: UserIn) -> User:
    user = storage.create_user(**user_in.model_dump())
    return user


def get_user_by_id(user_id: int) -> User | None:
    return storage.users.get(user_id)
