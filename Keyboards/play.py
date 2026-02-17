from aiogram.types import (
ReplyKeyboardMarkup,
KeyboardButton
)


Play_KB = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text = "кубик"),

            KeyboardButton(text = "дартс"),

            KeyboardButton(text = "слоты")
        ]
    ],

    one_time_keyboard = True,
    sellective = True,
    resize_keyboard = True,
    input_field_placeholder = "выбери мини-игру"

)
