from aiogram import executor

from create_bot import dp
from handlers import start


async def on_startup(_):
    print("Online")


start.reg_handlers(dp)


# if __name__ == "__main__":
executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
