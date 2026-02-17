#комманды
from aiogram.filters import Command, CommandObject, CommandStart
from aiogram.types import Message
from aiogram import Router

from Keyboards import mainKB

router = Router()

#помощь
@router.message(Command("help"))
async def HELP(message: Message):
    await message.answer("/действия - вызывает меню действий, 'кубик' - игра с кубиком, 'дартс' - игра в дартс, 'слоты' - слот машина")

#сообщение при команде старт
@router.message(Command("start"))
async def START(message: Message):
    await message.answer(f"здаров, {message.from_user.first_name}")

#выводит клавиатуру
@router.message(Command("действия"))
async def ACTIONS(message: Message):
    await message.answer("выбери действие", reply_markup = mainKB.main_kb)

