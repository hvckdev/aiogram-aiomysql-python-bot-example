from aiogram import Dispatcher, Bot
from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, loop=config.loop)
