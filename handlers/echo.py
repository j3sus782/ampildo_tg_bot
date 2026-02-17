#эхо
import random
from aiogram import Router, F, types, Bot
from aiogram.types import Message, FSInputFile

from Memory.text_Memory import INSERT
from Memory.text_getter import get_random

from handlers.voice_handlers.Voice_handler import voice

from ampildo import bot

MGE_list = ['MGE', 'MGE2', 'MGE3', 'MGE4', 'MGE5', 'MGE6', 'MGE7', 'MGE8', 'MGE9', 'MGE10']

citate_list = [
    'Из проведённых 64-х боёв у меня 64 победы. Все бои были с ', 'Я живу, как карта ляжет. Ты живёшь, как ', 'Если пьянка неизбежна, то ', 'Гадалка подошла ко мне чтобы погадать, но не угадала что я ',
    'Если заблудился в лесу, ', 'Запомни: всего одна ошибка – и ты ', 'Как говорил мой дед, ', 'пиво,водка, турничок через часик я ', 'Понедельник еще не настал, а я уже', 'Алкоголь - враг чееловечества, но в библий сказано: ',
    'одна ошибка и ты ', 'какая разница кто с кем спит? главное что все ', 'я раньше работал курьером, только я разносил не посылки, а ', 'Однажды ты ', 'Однажды меня укусила гадюка, спустя четыре дня она ', 'Спросил время, отдали ',
    'Остановку знаешь? Я ', 'Если тебя незаслуженно обидели, вернись и ', 'Тот, кто знает… ', 'Если закрыть глаза - становится ', 'Твой потолок чей-то ', 'Когда я родился доктор подумал, что ', 'Будь как я, а то будешь как ', 'Не смотри, что ростом мал у меня в штанах ',
    'Не стоит меня поправлять, я не ', 'В комнате стояли трое - он, она и ', 'Первый боковой, второй ', 'Мне два раза повторять не надо, мне и первого ', 'Есть два типа людей - все и ', 'Лучше пернуть как медведь, чем как крыса ', 'Ночь не утро, потому что ночью темно ',
    'Нахер Лондон и Милан, в моем сердце ', 'Ты глядишь на меня - видишь черты лица. Я гляжу на тебя - вижу ', 'Я не держу обиды, я держу ', 'Мнение, как транспорт - у кого нет своего ']


async def RND_num():
    rand = random.randint(1,10)
    return rand

router = Router()

#Main
try:
    @router.message()
    async def echo(message: Message):

        # пихаем текст сообщений в БД
        if message.text:
            await INSERT(message.text)
            #отвечаем на сообщения


            change = await RND_num()

            match change:
                case 1:
                    #простой ответ
                    text = await get_random()
                    await message.answer(text)
                case 2:
                    #Склееный текст
                    text = (await get_random()) + " " + (await get_random())
                    await message.answer(text)
                case 3:
                    #втройне склееный текст
                    text = (await get_random()) + " " + (await get_random()) + " " + (await get_random())
                    await message.answer(text)
                case 4:
                    #вчетверне скленный текст
                    text = (await get_random()) + " " + (await get_random()) + " " + (await get_random()) + " " + (await get_random())
                    await message.answer(text)
                case 5:
                    #Голосовое
                    await voice(message)
except Exception as e:
    print(e)


if __name__ == "__main__":
    print("эхо в норме")
    echo(message="")
    RND_num()