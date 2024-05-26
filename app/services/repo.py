from aiocache import Cache
from motor.motor_asyncio import AsyncIOMotorDatabase
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.dao import SalaryDAO
from app.utils.get_settings import get_settings


settings = get_settings()


class Repo:
    def __init__(self, mongo_db: AsyncIOMotorDatabase, cache: Cache = None):
        self.salary_dao = SalaryDAO(mongo_db=mongo_db, collection_name="sample_collection")
