from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from src.telegram_bot_app.utils.texts import start_text
from src.telegram_bot_app.keyboards.inline_keyboards import start_keyboard

# Initiate router
router = Router()


# handling /start command
@router.message(CommandStart())
async def process_start_command(message: Message):
    user_name = message.from_user.username
    reply_text = start_text(user_name)
    keyboard = await start_keyboard()
    await message.answer(text=reply_text, reply_markup=keyboard)


# handling /help command
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text="Помогите")