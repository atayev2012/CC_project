from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

# request geolocation keyboard
location_keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    keyboard=[[KeyboardButton(text="Отправить моё местоположение", request_location=True)]]
    )

# remove any reply keyboard
hide_keyboard = ReplyKeyboardRemove(selective=False)