from aiogram import Router
from aiogram.filters import Command, CommandStart,Text
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU
from keyboards.keyboards import create_game_keyboard, create_start_keyboard
from aiogram import F
from services.services import generate_bot_answer, choose_winner

# Инициализируем роутер уровня модуля
router: Router = Router()


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'],
                         reply_markup=create_start_keyboard())


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])


#user choice, that he doesnt want play the game:
@router.message(F.text == LEXICON_RU['lets_go/dont_want'][1])
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['dont_want_answer'])


#Если клиент выбрал "Играем" значет передаем перечень кнопок на выбор:
@router.message(F.text == LEXICON_RU['lets_go/dont_want'][0])
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['make_choose'],
                         reply_markup=create_game_keyboard())

@router.message(Text(text=LEXICON_RU['variants']))
async def process_help_command(message: Message):
    user_answer = message.text
    bot_answer = generate_bot_answer()
    winner = choose_winner(bot_answer, user_answer)
    await message.answer(text=LEXICON_RU[winner],
                         reply_markup=create_start_keyboard())
