from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.types.callback_query import CallbackQuery
from src.telegram_bot_app.utils.texts import start_text
from src.telegram_bot_app.keyboards.inline_keyboards import start_keyboard
from src.telegram_bot_app.utils.callback_models import GenderCallback, StyleCallback

# Initiate router
router = Router()

# Gender select callback handler
@router.callback_query(GenderCallback.filter())
async def process_gender_select_press(callback: CallbackQuery, callback_data: GenderCallback):
    await callback.message.edit_text(text="Твой пол: " + callback_data.edit_text)
    await callback.answer()

# Style select callback handler
@router.callback_query(StyleCallback.filter())
async def process_style_select_press(callback: CallbackQuery, callback_data: StyleCallback):
    await callback.answer()