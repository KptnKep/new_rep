from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon import LEXICON_RU

btn_yes = KeyboardButton(text=LEXICON_RU['yes_button'])
btn_no = KeyboardButton(text=LEXICON_RU['no_button'])

yes_no_kb_buelder = ReplyKeyboardBuilder()

yes_no_kb_buelder.row(btn_yes, btn_no, width=2)

yes_no_kb = yes_no_kb_buelder.as_markup(one_time_keyboard=True, resize_keyboard=True)

# Создаем кнопки игровой клавиатуры
button_1 = KeyboardButton(text=LEXICON_RU['rock'])
button_2 = KeyboardButton(text=LEXICON_RU['scissors'])
button_3 = KeyboardButton(text=LEXICON_RU['paper'])

# Создаем игровую клавиатуру с кнопками "Камень 🗿",
# "Ножницы ✂" и "Бумага 📜" как список списков
game_kb = ReplyKeyboardMarkup(
    keyboard=[[button_1],
              [button_2],
              [button_3]],
    resize_keyboard=True
)