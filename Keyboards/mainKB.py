from aiogram.types import (
ReplyKeyboardMarkup,
KeyboardButton
)

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="мини-игры")

        ]
    ],
    resize_keyboard = True,
    one_time_keyboard = True,
    sellective = True,
    input_field_placeholder = "выбери действие"
)