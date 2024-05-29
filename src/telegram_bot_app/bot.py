from config import BOT_TOKEN
from aiogram import Bot, Dispatcher
from src.telegram_bot_app.handlers.user_command_handlers import router as commands_router
from src.telegram_bot_app.handlers.user_call_handlers import router as call_router
from src.telegram_bot_app.utils.texts import GENDER_TEXT, GENDERS, load_gender_and_style_info

async def run_bot():
    await load_gender_and_style_info(GENDER_TEXT, GENDERS)

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(commands_router)
    dp.include_router(call_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
