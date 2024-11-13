from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

tasdiqlash_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✔️ Tasdiqlash", callback_data="tasdiqlash"),
            InlineKeyboardButton(text="✖️ Rad etish", callback_data="rad_etish")
        ]
    ], resize_keyboard=True
)