import aiosqlite

max_msg = 20000

#Вставляем данные
async def INSERT(mesg : str):
    async with aiosqlite.connect('Memory/text.db') as connect:

        #Проверка достигнуто ли максимальное кол-во сообщений##
        result = await connect.execute('SELECT COUNT(*) FROM Messages')
        count = (await result.fetchone())[0]

        if count == max_msg:
            await connect.execute('DELETE FROM Messages WHERE id = (SELECT MIN(id) FROM Messages)')

            print("Удалено старое сообщение")
        ###

        #Вставляем сообщение в БД##
        await connect.execute('INSERT INTO Messages (message) VALUES(?)', (str(mesg),))

        await connect.commit()
        print("Успешно добавлено")
        ###

#очищение БД
async def delete_all():
    async with aiosqlite.connect('Memory/text.db') as connect:
        await connect.commit()

        await connect.execute("DELETE FROM Messages")
        await connect.commit()

        await connect.execute("VACUUM")
        await connect.commit()
        print("Успешно удалено все")

if __name__ == '__main__':
    print("вроде все в норме")
    INSERT(mesg = "")
    delete_all()