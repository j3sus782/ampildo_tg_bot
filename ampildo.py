#главный файл
import asyncio
import config
from handlers import appends, commands, echo
from aiogram import Bot, Dispatcher, F
from Memory import _init_


bot = Bot(config.token)

#Основная функция
async def main():
    dp = Dispatcher()

    #импортирует все роутеры из разделенных файлов
    dp.include_routers(
        appends.router,
        commands.router,


        echo.router
    )

    #удаляет вебхуки
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    print('бот запущен')
    #инициализация БД
    asyncio.run(_init_.init_db())
    #запуск бота
    asyncio.run(main())