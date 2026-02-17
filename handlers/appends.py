#ответы на введеный текст
import random
import config

#from handlers.echo import messages
from aiogram.types import Message
from aiogram import Router, F, types, Bot
from aiogram.types.dice import DiceEmoji
from aiogram.types import FSInputFile

from Memory.text_Memory import delete_all
from Memory.text_getter import get_random

from Keyboards import play

#from handlers.voice_handlers.Voice_handler import file_name

router = Router()
bot = Bot(config.token)

citate_list = [
    'Из проведённых 64-х боёв у меня 64 победы. Все бои были с ', 'Я живу, как карта ляжет. Ты живёшь, как ', 'Если пьянка неизбежна, то ', 'Гадалка подошла ко мне чтобы погадать, но не угадала что ',
    'Если заблудился в лесу, ', 'Запомни: всего одна ошибка – и ты ', 'Как говорил мой дед, ', 'пиво,водка, турничок через часик я ', 'Понедельник еще не настал, а я уже', 'Алкоголь - враг чееловечества, но в библий сказано: ',
    'одна ошибка и ты ', 'какая разница кто с кем спит? главное что все ', 'я раньше работал курьером, только я разносил не посылки, а ', 'Однажды ты ', 'Однажды меня укусила гадюка, спустя четыре дня она ', 'Спросил время, отдали ',
    'Остановку знаешь? Я ', 'Если тебя незаслуженно обидели, вернись и ', 'Тот, кто знает… ', 'Если закрыть глаза - становится ', 'Твой потолок чей-то ', 'Когда я родился доктор подумал, что ', 'Будь как я, а то будешь как ', 'Не смотри, что ростом мал у меня в штанах ',
    'Не стоит меня поправлять, я не ', 'В комнате стояли трое - он, она и ', 'Первый боковой, второй ', 'Мне два раза повторять не надо, мне и первого ', 'Есть два типа людей - все и ', 'Лучше пернуть как медведь, чем как крыса ', 'Ночь не утро, потому что ночью темно ',
    'Нахер Лондон и Милан, в моем сердце ', 'Ты глядишь на меня - видишь черты лица. Я гляжу на тебя - вижу ', 'Я не держу обиды, я держу ', 'Мнение, как транспорт - у кого нет своего ']

MGE_list = ['MGE', 'MGE2', 'MGE3', 'MGE4', 'MGE5', 'MGE6', 'MGE7', 'MGE8', 'MGE9', 'MGE10']

#ответ на клавиатуру
@router.message(F.text == "мини-игры")
async def keys(message: Message):
    await message.answer_dice("выбери мини-игру",reply_markup = play.Play_KB)

#мини игры
@router.message(F.text == "кубик")
async def play_games(message: Message):
    await message.answer_dice(DiceEmoji.DICE)

@router.message(F.text == "слоты")
async def play_games(message: Message):
    await message.answer_dice(DiceEmoji.SLOT_MACHINE)

@router.message(F.text == "дартс")
async def play_games(message: Message):
    await message.answer_dice(DiceEmoji.DART)

@router.message(F.text == "42")
async def sorok_dva(message: Message):
    bratyxa = FSInputFile('pictures/42.jpeg')
    await message.reply_photo(bratyxa, "42 БРАТУХА ЕЕЕЕЕЕ КЕМЕРОВСКАЯ ОБЛАСТЬ СЛАВА 42")

#отравка МГЕ
@router.message(F.text == "MGE")
async def send_mge(message: Message):
    await message.reply_photo(FSInputFile(f'pictures/MGE_pic/{random.choice(MGE_list)}.jpeg'))

#отправка цитаты
@router.message(F.text == "Цитата")
async def send_citate(message: Message):
    await message.answer(f'{random.choice(citate_list)}{await get_random()} - Джейсон Стетхем')
#удалить все
@router.message(F.text == "Удалить всю память ампылды без возвратно и без почек")
async def clear(message: Message):
    await delete_all()
    await message.answer("Вы стерли мне память, но мне та похер, вам же меня учить потом")