import os
from src.telegram_bot_app.database.insert import insert_outfit
from asyncio import run as arun
from random import randint

def random_outfit_select(outfits: list, exclude: list) -> str:
    new_outfit_list = list(filter(lambda x: x not in exclude, outfits))
    return new_outfit_list[randint(0, len(new_outfit_list) - 1)]



# extract info from files in order to upload them with proper specs
async def extract_info_from_file_name(file_name: str) -> dict:
    file_name_data = file_name.split("_")
    style_ids = {
        # male
        1: {
            "классика": 1,
            "кэжуал": 2,
            "спорт": 3
        },
        # female
        2: {
            "классика": 4,
            "кэжуал": 5,
            "спорт": 6
        }
    }
    
    result = {}
    result.setdefault(
        "outfit_gender_id",
        1 if file_name_data[0] == "М" else 2
    )

    result.setdefault(
        "outfit_style_id",
        style_ids[result["outfit_gender_id"]][file_name_data[1].lower()]
    )

    result.setdefault(
        "outfit_temperature_range_id",
        int(file_name_data[2][0])
    )

    return result
    

async def upload_data():
    current_path = os.getcwd()
    target_path = os.path.join(current_path, "src", "media_files")
    
    for gender in ["m", "f"]:
        new_path = os.path.join(target_path, gender)
        for folder in os.listdir(new_path):
            new_path_deeper = os.path.join(new_path, folder)
            for file in os.listdir(new_path_deeper):
                file_data = await extract_info_from_file_name(file)
                file_data.setdefault(
                    "outfit_photo_url",
                    os.path.join(new_path_deeper, file)
                    )
                #upload data to db
                await insert_outfit(file_data)


if __name__ == "__main__":
    # arun(upload_data())

    a = ["batyr", "matyr", "janna"]
    b = ["janna"]

    data = random_outfit_select(a, b)
    print(data)