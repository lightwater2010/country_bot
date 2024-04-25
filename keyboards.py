from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb = ReplyKeyboardMarkup(keyboard=[[
    KeyboardButton(text="/search")
]], resize_keyboard=True)