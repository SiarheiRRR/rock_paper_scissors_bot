from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon import lexicon_ru


def create_game_keyboard():
    kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
    buttons: tuple[KeyboardButton] = tuple(KeyboardButton(text=button) for button in lexicon_ru.LEXICON_RU['variants'])
    kb_builder.row(*buttons, width=3)
    return kb_builder.as_markup(resize_keyboard=True)

def create_start_keyboard():
    kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
    buttons: tuple[KeyboardButton] = tuple(KeyboardButton(text=button)
                                           for button in lexicon_ru.LEXICON_RU['lets_go/dont_want'])
    kb_builder.row(*buttons, width=2)
    return kb_builder.as_markup(resize_keyboard=True)
