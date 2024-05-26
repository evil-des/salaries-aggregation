import typing

from aiogram.filters import Filter
from aiogram.types import Message
from app.services.repo import Repo
import json


class JSONFilter(Filter):
    async def __call__(self, message: Message, repo: Repo) -> bool:
        try:
            json.loads(message.text)
        except ValueError as e:
            await message.answer("Получен неверный формат!")
            return False
        return True
