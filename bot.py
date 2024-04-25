import asyncio

from aiogram import Bot, Dispatcher
from handlers import router
from config import Token

bot = Bot(Token)
disp = Dispatcher()

async def main():
    disp.include_router(router=router)
    await disp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())