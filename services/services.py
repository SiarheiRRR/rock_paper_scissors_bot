from random import choice
from lexicon.lexicon_ru import LEXICON_RU


def generate_bot_answer():
    return choice(LEXICON_RU['variants'])

#['Камень', 'Ножницы', 'Бумага'],
#['Камень', 'Ножницы', 'Бумага'],
#['Камень', 'Ножницы', 'Бумага'],
#'Камень', 'Ножницы'
#'Ножницы', 'Бумага'
#'Бумага', 'Камень'


def choose_winner(bot_answer, user_answer):
    if bot_answer == user_answer:
        return 'draw'
    elif (bot_answer, user_answer) in LEXICON_RU['winner_combinations']:
        return 'bot_winner'
    return 'user_winner'

