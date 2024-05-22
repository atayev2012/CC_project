# user_name - username in telegram app, user_status - if user purchased premium
def start_text(user_name: str, user_status: str = "free") -> str:
    result_text = f"Привет @{user_name}! Я - твой личный помощник в выборе одежды."
    if user_status == "free":
        result_text += (f"\nПодключи премиум 👑 или попробуй бесплатно 🆓\n\n"
                       f"Бесплатный вариант: только 1 запрос в день, один аутфит\n\n"
                       f"Премиум: безлимит запросов, два аутфита")

    return result_text


# texts for /gender command
GENDER_TEXT = "Твой пол?👚👕"
GENDERS = {
    "m": "👕 Мужской",
    "f": "👚 Женский"
}

# texts for /style command
STYLE_TEXT = "Какой стиль ты предпочитаешь?"
