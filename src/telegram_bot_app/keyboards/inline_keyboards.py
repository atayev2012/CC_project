from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from src.telegram_bot_app.utils.callback_models import GenderCallback, GetOutfitCallback
from src.telegram_bot_app.utils.callback_models import (GENDER_MALE, GENDER_FEMALE, GENDER_FEMALE_FREE, GENDER_MALE_FREE, GET_OUTFIT, GET_FREE_OUTFIT,
                                                        MALE_STYLE_1, MALE_STYLE_2, MALE_STYLE_3, MALE_STYLE_FREE_1, MALE_STYLE_FREE_2, MALE_STYLE_FREE_3,
                                                        FEMALE_STYLE_1, FEMALE_STYLE_2, FEMALE_STYLE_3, FEMALE_STYLE_FREE_1, FEMALE_STYLE_FREE_2,
                                                        FEMALE_STYLE_FREE_3)


# if user is free suggest to buy premium or continue for free
# start keyboard
async def start_keyboard(is_premium: bool = False) -> InlineKeyboardMarkup:
    if not is_premium:
        start_keyboard_markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="👑 Подключить премиум", callback_data="xpremium")],
                [InlineKeyboardButton(text="🆓 Подобрать аутфит", callback_data=GET_FREE_OUTFIT)]
            ]
        )
    else:
        start_keyboard_markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Подобрать аутфит", callback_data=GET_OUTFIT)]
            ]
        )
    return start_keyboard_markup

# gender select keyboard
async def gender_keyboard(is_premium: bool = False) -> InlineKeyboardMarkup:
    if is_premium:
        gender_keyboard_markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Женский", callback_data=GENDER_FEMALE)],
                [InlineKeyboardButton(text="Мужской", callback_data=GENDER_MALE)]
            ]
        )
    else:
        gender_keyboard_markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Женский", callback_data=GENDER_FEMALE_FREE)],
                [InlineKeyboardButton(text="Мужской", callback_data=GENDER_MALE_FREE)]
            ]
        )

    return gender_keyboard_markup


# rate photo keyboard
async def rate_photo_keyboard(photo_id: int) -> InlineKeyboardMarkup:
    photo_keyboard = InlineKeyboardBuilder()
    photo_keyboard.row(
        *[
            InlineKeyboardButton(text="\u2b50", callback_data=f"c1{photo_id}"),
            InlineKeyboardButton(text="\u2b50", callback_data=f"c2{photo_id}"),
            InlineKeyboardButton(text="\u2b50", callback_data=f"c3{photo_id}"),
            InlineKeyboardButton(text="\u2b50", callback_data=f"c4{photo_id}"),
            InlineKeyboardButton(text="\u2b50", callback_data=f"c5{photo_id}")
        ], 
        width=5
    )

    return photo_keyboard.as_markup()

# style keyboard
async def style_keyboard(gender: str, is_premium: bool = False) -> InlineKeyboardMarkup:
    if is_premium:
        if gender == "m":
            style_keyboard_markup = InlineKeyboardMarkup(
                inline_keyboard=[
                    [InlineKeyboardButton(text="Классика", callback_data=MALE_STYLE_1)],
                    [InlineKeyboardButton(text="Кэжуал", callback_data=MALE_STYLE_2)],
                    [InlineKeyboardButton(text="Спорт", callback_data=MALE_STYLE_3)]
                ]
        )
        else:
            style_keyboard_markup = InlineKeyboardMarkup(
                inline_keyboard=[
                    [InlineKeyboardButton(text="Классика", callback_data=FEMALE_STYLE_1)],
                    [InlineKeyboardButton(text="Кэжуал", callback_data=FEMALE_STYLE_2)],
                    [InlineKeyboardButton(text="Спорт", callback_data=FEMALE_STYLE_3)]
                ]
        )
    else:
        if gender == "m":
            style_keyboard_markup = InlineKeyboardMarkup(
                inline_keyboard=[
                    [InlineKeyboardButton(text="Классика", callback_data=MALE_STYLE_FREE_1)],
                    [InlineKeyboardButton(text="Кэжуал", callback_data=MALE_STYLE_FREE_2)],
                    [InlineKeyboardButton(text="Спорт", callback_data=MALE_STYLE_FREE_3)]
                ]
        )
        else:
            style_keyboard_markup = InlineKeyboardMarkup(
                inline_keyboard=[
                    [InlineKeyboardButton(text="Классика", callback_data=FEMALE_STYLE_FREE_1)],
                    [InlineKeyboardButton(text="Кэжуал", callback_data=FEMALE_STYLE_FREE_2)],
                    [InlineKeyboardButton(text="Спорт", callback_data=FEMALE_STYLE_FREE_3)]
                ]
        )
    return style_keyboard_markup
# start keyboard

