from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, ContentType, InputFile, BufferedInputFile
from src.telegram_bot_app.utils.texts import start_text, GENDER_TEXT
from src.telegram_bot_app.keyboards.inline_keyboards import start_keyboard, gender_keyboard, rate_photo_keyboard
from src.telegram_bot_app.keyboards.reply_keyboards import hide_keyboard
from src.telegram_bot_app.database.select import select_user, select_temp_info, select_temperature_range, select_outfit
from src.telegram_bot_app.database.insert import insert_user
from src.weather_app.tomorrow_io import request_weather
from src.weather_app.temperature_calculator import daily_temperature
from datetime import datetime
import math
from aiogram.types import ReplyKeyboardRemove
from src.telegram_bot_app.bot import Bot
from random import randint

async def random_outfit_select(outfits: list, exclude: list) -> str:
    new_outfit_list = list(filter(lambda x: x not in exclude, outfits))
    return new_outfit_list[randint(0, len(new_outfit_list) - 1)]

# Initiate router
router = Router()


# handling /start command
@router.message(CommandStart())
async def process_start_command(message: Message):
    # get user id
    user_id = message.from_user.id

    # check database for user
    user_data = await select_user(user_id)

    # if user does not exist add it to database
    if not user_data:
        user_data = {
            "id": user_id,
            "user_name": message.from_user.username,
            "first_name": message.from_user.first_name,
            "last_name": message.from_user.last_name,
            "is_premium": False
        }

        await insert_user(user_data)
    
    # Send star message
    reply_text = await start_text(user_data["user_name"], user_data["is_premium"])
    keyboard = await start_keyboard(user_data["is_premium"])
    await message.answer(text=reply_text, reply_markup=keyboard)


# handling /help command
@router.message(Command(commands="help"))
async def process_help_command(message: Message):
    photo_buffer = BufferedInputFile.from_file("/home/batyr/Desktop/Minor project/CC_project/src/media_files/m/casual/М_Кэжуал_5.jpg")
    await message.answer_photo(photo_buffer)
    


# # handling /gender command
# @router.message(Command(commands="gender"))
# async def process_gender_command(message: Message):
#     reply_text = GENDER_TEXT[0]
#     keyboard = await gender_keyboard()
#     await message.answer(text=reply_text, reply_markup=keyboard)

@router.message(F.content_type == ContentType.LOCATION)
async def process_location_handler(message: Message):
    lat = message.location.latitude
    lon = message.location.longitude
    
    # load temporary data
    temp_user_info = await select_temp_info(message.from_user.id)
    current_time = datetime.now()
    forecast_hours = 24 - current_time.hour if current_time.hour <= 12 else 12
    
    # after getting information from weather website, need to check if it was successfull
    weather_tomorrow_io = request_weather(lat, lon, forecast_hours)
    
    if weather_tomorrow_io:
        weather_dict = daily_temperature(weather_tomorrow_io)

        # send message saying what temperature it is
        temperature_data = await select_temperature_range(weather_dict["average_real_feel"])
        await message.answer(text=f"На улице {math.ceil(weather_dict['current_temperature'])}°C\n{temperature_data['temperature_text']}{temperature_data['temperature_emoji']}", reply_markup=ReplyKeyboardRemove())
        

        
        # load all photo paths
        files = await select_outfit(temp_user_info["style_id"], temperature_data["id"])
        
        photos = []
        photos.append(await random_outfit_select(files, []))
        
        # if temp_user_info["is_premium"]:
        #     photos.append(await random_outfit_select(files, photos)) 

        #     # send message about outfitsof the day
        #     await message.answer(text="Аутфиты дня:")

        await message.answer(text="Аутфит дня:")

        for photo in photos:
            photo_buffer = BufferedInputFile.from_file(photo)
            await message.answer_photo(photo_buffer)
