from aiogram.filters.callback_data import CallbackData


# ================== Start Gender Select ===================

# Gender Class
class GenderCallback(CallbackData, prefix="gender"):
    gender: str
    edit_text: str

# Gender Models
GENDER_MALE = GenderCallback(
    gender="m",
    edit_text="👕 Мужской!"
).pack()
GENDER_FEMALE = GenderCallback(
    gender="f",
    edit_text="👚 Женский!"
).pack()

# ==================== End Gender Select ===================

# =================== Start Style Select ===================
# Gender Class
class StyleCallback(CallbackData, prefix="style"):
    style: str
    edit_text: str

# Style models


# ==================== End Style Select ====================