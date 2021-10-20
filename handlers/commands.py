from aiogram import types
import utils.db_api.db
from dispatcher import dp


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(await utils.db_api.db.commands.get_rows())
