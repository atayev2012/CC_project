from config import BOT_TOKEN
from aiogram import Bot, Dispatcher
from src.telegram_bot_app.handlers.user_command_handlers import router as commands_router

async def run_bot():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(commands_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
