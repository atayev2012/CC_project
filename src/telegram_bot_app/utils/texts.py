from src.telegram_bot_app.database.select import select_all_genders_info
# user_name - username in telegram app, user_status - if user purchased premium
async def start_text(user_name: str, is_premium: bool = False) -> str:
    result_text = f"Привет @{user_name}! Я - твой личный помощник в выборе одежды."
    if not is_premium:
        result_text += (f"\nПодключи премиум 👑 или попробуй бесплатно 🆓\n\n"
                       f"Бесплатный вариант: только 1 запрос в день, один аутфит\n\n"
                       f"Премиум: безлимит запросов, два аутфита")

    return result_text


# texts for /gender command
async def load_gender_and_style_info(gender_text: list, genders: dict):
    temp_genders = await select_all_genders_info()
    gender_text.append(f"Твой пол? {''.join([x['gender_emoji'] for x in temp_genders.values()])}")

    for key in temp_genders:
        genders.setdefault(key, {
            f"{temp_genders[key]['gender_emoji']} {temp_genders[key]['gender_full_name']}"
        })

GENDER_TEXT = []
GENDERS = {}

# texts for /style command
STYLE_TEXT = "Какой стиль ты предпочитаешь?"
# Clothing styles
STYLES = {
    # male
    "m": {
        "Классика": "classic",
        "Кэжуал": "casual",
        "Спорт": "sport"
    },
    # female
    "f": {
        "Классика": "classic",
        "Кэжуал": "casual",
        "Спорт": "sport"
    }
}

STYLES_ID = {
    # male
    "m": {
        "Классика": 1,
        "Кэжуал": 2,
        "Спорт": 3
    },
    # female
    "f": {
        "Классика": 4,
        "Кэжуал": 5,
        "Спорт": 6
    }
}

GEO_TEXT = "Отлично! Теперь поделись своим местоположением 📍"