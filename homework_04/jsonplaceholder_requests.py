"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import logging
from typing import List, Dict

from aiohttp import ClientSession

log = logging.getLogger(__name__)

BASE_URL = "https://jsonplaceholder.typicode.com"
USERS_DATA_URL = f"{BASE_URL}/users"
POSTS_DATA_URL = f"{BASE_URL}/posts"


async def fetch_json(url: str):
    async with ClientSession() as session:
        async with session.get(url, timeout=60) as response:
            data = await response.json()
            return data


async def fetch_users_data(url: str = USERS_DATA_URL) -> List[Dict]:
    return await fetch_json(url)


async def fetch_posts_data(url: str = POSTS_DATA_URL) -> List[Dict]:
    return await fetch_json(url)
