from src.weather_app.tomorrow_io import request_weather
from src.weather_app.temperature_calculator import daily_temperature
from datetime import datetime
from pprint import pprint
from src.telegram_bot_app.bot import run_bot
import asyncio
from src.telegram_bot_app.database.select import select_user, select_all_genders_info
from src.telegram_bot_app.database.insert import insert_user, insert_gender, insert_style, insert_temperature_range, insert_outfit
import os
from src.telegram_bot_app.utils.texts import STYLES_ID, STYLES

# async def run_data():
    # result = await select_user(2)
    # print(result)


# asyncio.run(run_data())
asyncio.run(run_bot())
# async def upload_data():
#     file_names = {"m": [], "f":[]}
#     current_path = os.getcwd()
#     target_path = os.path.join(current_path, "src", "media_files")

#     for key in file_names:
#         new_path = os.path.join(target_path, key)
#         for folder in os.listdir(new_path):
#             new_path_deeper = os.path.join(new_path, folder)
#             for file in os.listdir(new_path_deeper):
#                 file_names[key].append(os.path.join(new_path_deeper, file))


#     style_val = {
#         "classic": "Классика",
#         "sport": "Спорт",
#         "casual": "Кэжуал"
#     }

#     for key in file_names:
#         for file in file_names[key][1:]:
#             for style in style_val:
#                 if style in file:
#                     style_id_hint = style_val[style]
#             upload_data = {
#                 "outfit_photo_url": file,
#                 "outfit_gender_id": 1 if key == "m" else 2,
#                 "outfit_style_id": STYLES_ID[key][style_id_hint]
#             }

#             await insert_outfit(upload_data)

# asyncio.run(upload_data())
# data = request_weather(, )

# for item in data:
#     print(item)

# ===========================================================

# current_time = datetime.now()
# forecast_hours = 24 - current_time.hour if current_time.hour <= 12 else 12

# lat = 56.2961
# loc = 44.0418

# # for i in range(100):
# #     print(f"{i+1}. ", end="")
# weather_data = request_weather(lat, loc, forecast_hours)

# pprint(weather_data)
# print()
# values = daily_temperature(weather_data)
# print(values)
