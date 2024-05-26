from typing import List, Optional
from aiogram import types
from bson import ObjectId
from pymongo import ASCENDING

from app.services.dao.base import DAO


class SalaryDAO(DAO):
    async def get_record_by_id(self, id: str):
        res = self.collection.find_one({'_id': ObjectId(id)})
        return await res.fetch
        # return await self.collection.find_one({'_id': ObjectId(id)})

    async def aggregate(self):
        res = self.collection.aggregate([
            {
                "$sort": {"value": ASCENDING}
            }
        ])
        return await res.to_list(length=20)