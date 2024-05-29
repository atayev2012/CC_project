from aiogram.filters.callback_data import CallbackData



# ================== Start Select Outfit ===================
# Get Outfit Class
class GetOutfitCallback(CallbackData, prefix="outfit"):
    is_premium: bool

# Get Outfit Models
GET_FREE_OUTFIT = GetOutfitCallback(is_premium=False).pack()
GET_OUTFIT = GetOutfitCallback(is_premium=True).pack()

# ==================== End Select Outfit ===================


# ================== Start Gender Select ===================

# Gender Class
class GenderCallback(CallbackData, prefix="gender"):
    gender: str
    edit_text: str
    is_premium: bool

# Gender Models
GENDER_MALE = GenderCallback(
    gender = "m",
    edit_text = "👕 Мужской!",
    is_premium = True
).pack()

GENDER_FEMALE = GenderCallback(
    gender = "f",
    edit_text = "👚 Женский!",
    is_premium = True
).pack()

GENDER_MALE_FREE = GenderCallback(
    gender = "m",
    edit_text = "👕 Мужской!",
    is_premium = False
).pack()

GENDER_FEMALE_FREE = GenderCallback(
    gender = "f",
    edit_text = "👚 Женский!",
    is_premium = False
).pack()

# ==================== End Gender Select ===================

# =================== Start Style Select ===================
# Gender Class
class StyleCallback(CallbackData, prefix="style"):
    style: str
    gender: str
    is_premium: bool

# Style models
MALE_STYLE_FREE_1 = StyleCallback(
    style="Классика",
    gender="m",
    is_premium=False
).pack()

MALE_STYLE_1 = StyleCallback(
    style="Классика",
    gender="m",
    is_premium=True
).pack()

MALE_STYLE_FREE_2 = StyleCallback(
    style="Кэжуал",
    gender="m",
    is_premium=False
).pack()

MALE_STYLE_2 = StyleCallback(
    style="Кэжуал",
    gender="m",
    is_premium=True
).pack()

MALE_STYLE_FREE_3 = StyleCallback(
    style="Спорт",
    gender="m",
    is_premium=False
).pack()

MALE_STYLE_3 = StyleCallback(
    style="Спорт",
    gender="m",
    is_premium=True
).pack()

FEMALE_STYLE_FREE_3 = StyleCallback(
    style="Спорт",
    gender="f",
    is_premium=False
).pack()

FEMALE_STYLE_3 = StyleCallback(
    style="Спорт",
    gender="f",
    is_premium=True
).pack()

FEMALE_STYLE_FREE_1 = StyleCallback(
    style="Классика",
    gender="f",
    is_premium=False
).pack()

FEMALE_STYLE_1 = StyleCallback(
    style="Классика",
    gender="f",
    is_premium=True
).pack()

FEMALE_STYLE_FREE_2 = StyleCallback(
    style="Кэжуал",
    gender="f",
    is_premium=False
).pack()

FEMALE_STYLE_2 = StyleCallback(
    style="Кэжуал",
    gender="f",
    is_premium=True
).pack()


# ==================== End Style Select ====================