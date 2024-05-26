import abc

from aiocache import Cache
from motor.motor_asyncio import AsyncIOMotorDatabase, AsyncIOMotorCollection


class DAO(abc.ABC):
    def __init__(
        self,
        mongo_db: AsyncIOMotorDatabase,
        collection_name: str,
        cache: Cache | None = None
    ):
        self.db = mongo_db
        self.collection = self.db[collection_name]

        self.cache = cache
