from aiogram import types, Dispatcher

from create_bot import bot
from key_board import kb
from weather_api import give_forecast

bot_replies = {
    "start": "Hi, I can help you to know the weather!. Pick any commands from buttons.",
    "help": "In order to get a forecast, enter the command /forecast with your current longitude and latitude: /forecast long lat",
    "schedule": "Enter a time, when you want to get your weather forecast",
    "forecast":  "Please enter your long and lat.",
}

# Test handler
async def greetings(message: types.Message):
    await bot.send_message(message.from_user.id, bot_replies["start"], reply_markup=kb)

# Test handler
async def help(message: types.Message):
    await bot.send_message(message.from_user.id, bot_replies["help"])

# Test handler
async def schedule(message: types.Message):
    await bot.send_message(message.from_user.id, bot_replies["schedule"])

# Handler for a command for manual enter of latitude and longitude of a user
async def forecast(message: types.Message):
    user_input = message.text.split()
    await bot.send_message(message.from_user.id, text=give_forecast(lat=user_input[1], long=user_input[2]))


def reg_handlers(dp: Dispatcher):
    dp.register_message_handler(greetings, commands=["start"])
    dp.register_message_handler(help, commands=["help"])
    dp.register_message_handler(schedule, commands=["schedule"])
    dp.register_message_handler(forecast, commands=["forecast"])
