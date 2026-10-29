import asyncio
from aiogram import Bot, Dispatcher
from aiogram.exceptions import (
    TelegramNetworkError,
)
from config.settings import BOT_TOKEN
from handlers.users.start import rt as start
from handlers.users.mushuk import rt as mushuk
from handlers.users.photo import rt as photo
from handlers.users.video import rt as video
from handlers.users.dice import rt as dice
from handlers.users.start import rt as animation
from handlers.users.animation import  rt as text
from handlers.users.hammasi import rt as hammasi
from handlers.users.test import rt as test
dp = Dispatcher()
async def main():
    bot = Bot(BOT_TOKEN)

    dp.include_router(start)
    dp.include_router(photo)
    dp.include_router(mushuk)
    dp.include_router(video)
    dp .include_router(dice)
    dp.include_router(animation)
    dp.include_router(text)
    dp.include_router(hammasi)
    dp.include_router(test)

    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        print("bot ishga tushdi")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("bot to'xtatildi")
    except TelegramNetworkError:
        print("internetga ulang")
