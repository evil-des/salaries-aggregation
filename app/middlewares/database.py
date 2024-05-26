from typing import Any, Awaitable, Callable, Dict

from aiocache import Cache
from aiogram import BaseMiddleware
from aiogram.types import Message
from motor.motor_asyncio import AsyncIOMotorDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from app.services.repo import Repo


class DatabaseMiddleware(BaseMiddleware):
    def __init__(self, mongo_db: AsyncIOMotorDatabase, cache: Cache):
        super().__init__()
        self.mongo_db = mongo_db
        self.cache = cache

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        data["repo"] = Repo(cache=self.cache, mongo_db=self.mongo_db)
        return await handler(event, data)
