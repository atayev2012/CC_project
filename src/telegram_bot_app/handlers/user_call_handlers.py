from aiogram import Router
from aiogram.types.callback_query import CallbackQuery
from src.telegram_bot_app.utils.texts import start_text, GENDER_TEXT, STYLE_TEXT, GEO_TEXT
from src.telegram_bot_app.keyboards.inline_keyboards import start_keyboard, rate_photo_keyboard, gender_keyboard, style_keyboard
from src.telegram_bot_app.keyboards.reply_keyboards import location_keyboard
from src.telegram_bot_app.utils.callback_models import GenderCallback, StyleCallback, GetOutfitCallback
from src.telegram_bot_app.database.select import select_all_genders_info, select_temp_info
from src.telegram_bot_app.database.insert import insert_temp_info
from src.telegram_bot_app.database.update import update_temp_info
from src.telegram_bot_app.utils.texts import STYLES_ID

# Initiate router
router = Router()

# Select outfit callback handler
@router.callback_query(GetOutfitCallback.filter())
async def process_get_outfit_press(callback: CallbackQuery, callback_data: GetOutfitCallback):
    reply_text = GENDER_TEXT[0]
    gender_select_keyboard = await gender_keyboard(callback_data.is_premium)
    await callback.message.edit_text(text=reply_text, reply_markup=gender_select_keyboard)
    await callback.answer()


# Gender select callback handler
@router.callback_query(GenderCallback.filter())
async def process_gender_select_press(callback: CallbackQuery, callback_data: GenderCallback):
    await callback.message.edit_text(text="Твой пол: " + callback_data.edit_text)
    await callback.answer()

    # Send new message to request for style
    reply_text = STYLE_TEXT
    style_select_keyboard = await style_keyboard(callback_data.gender, callback_data.is_premium)
    await callback.message.answer(text=reply_text, reply_markup=style_select_keyboard)



# Style select callback handler
@router.callback_query(StyleCallback.filter())
async def process_style_select_press(callback: CallbackQuery, callback_data: StyleCallback):
    await callback.message.edit_text(text="Твой стиль: " + callback_data.style)
    temp_user_info = {
        "user_id": callback.message.chat.id,
        "is_premium": callback_data.is_premium,
        "gender": callback_data.gender,
        "style_id": STYLES_ID[callback_data.gender][callback_data.style]
    }
    # check if data already exist
    temp_user_not_exist = await select_temp_info(temp_user_info["user_id"])

    if temp_user_not_exist:
        await update_temp_info(temp_user_info)
    else:
        await insert_temp_info(temp_user_info)

    await callback.answer()

    # Send new message to request for geolocation
    reply_text = GEO_TEXT
    await callback.message.answer(text=reply_text, reply_markup=location_keyboard)




