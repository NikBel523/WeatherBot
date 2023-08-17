from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Test keys
start_b = KeyboardButton("/start")
help_b = KeyboardButton("/help")
forecast_b = KeyboardButton("/forecast")
schedule_b = KeyboardButton("/schedule")

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.row(start_b, help_b).row(forecast_b, schedule_b)
