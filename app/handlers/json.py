from aiogram import F, Router, types
from aiogram.filters import Command
from app.services.repo import Repo
from app.filters import JSONFilter

router = Router()


@router.message(JSONFilter())
async def json_handler(message: types.Message, repo: Repo) -> None:
    test = await repo.salary_dao.aggregate()
    await message.answer(str(test))
    # print(test)
    # await message.answer(str(test))

