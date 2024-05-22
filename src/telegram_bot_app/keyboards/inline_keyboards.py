from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# if user is free suggest to buy premium or continue for free
# start keyboard
async def start_keyboard(user_status: str = "free") -> InlineKeyboardMarkup:
    if user_status == "free":
        start_keyboard_markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="👑 Подключить премиум", callback_data="xpremium")],
                [InlineKeyboardButton(text="🆓 Продолжить бесплатно", callback_data="xfree")]
            ]
        )
    else:
        start_keyboard_markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Подобрать аутфит", callback_data="outfit")]
            ]
        )
    return start_keyboard_markup

# gender select keyboard
# async def gender_keyboard(from_start=False) -> InlineKeyboardMarkup:
#     gender_keyboard_markup = InlineKeyboardMarkup()
#     gender_keyboard_markup.row_width = 2
#     if from_start:
#         gender_keyboard_markup.add(
#             InlineKeyboardButton("Женский", callback_data="fs"),
#             InlineKeyboardButton("Мужской", callback_data="ms")
#         )
#     else:
#         gender_keyboard_markup.add(
#             InlineKeyboardButton("Женский", callback_data="fn"),
#             InlineKeyboardButton("Мужской", callback_data="mn")
#         )

#     return gender_keyboard_markup


# style keyboard

# start keyboard

