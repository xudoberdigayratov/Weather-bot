from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

myList = [
    "Andijon viloyati",
    "Buxoro viloyati",
    "Fargona viloyati",
    "Jizzax viloyati",
    "Namangan viloyati",
    "Navoiy viloyati",
    "Qashqadaryo viloyati",
    "Samarqand viloyati",
    "Sirdaryo viloyati",
    "Surxondaryo viloyati",
    "Toshkent viloyati",
    "Xorazm viloyati",
]


def menu():
    keyboard = InlineKeyboardMarkup(row_width=2)
    buttons = []
    for x in myList:
        buttons.append(InlineKeyboardButton(text=x, callback_data=f"pogoda_{x.replace(' viloyati', '')}"))

    keyboard.add(*buttons)
    return keyboard


back = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Orqaga', callback_data="back")
        ]
    ]
)
