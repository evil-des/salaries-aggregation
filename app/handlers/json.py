from aiogram import F, Router, types
from aiogram.filters import Command
from app.services.repo import Repo
from app.filters import JSONFilter
from app.models import InputData, GroupType
from datetime import datetime
import json

router = Router()


@router.message(JSONFilter())
async def json_handler(message: types.Message, repo: Repo) -> None:
    json_input = json.loads(message.text.strip())

    if json_input.get("group_type").lower() not in ["hour", "day", "month"]:
        await message.answer("Неверный формат!")
        return

    input_data = InputData(**json_input)
    data = await repo.salary_dao.aggregate(input_data)

    await message.answer(str(data))
