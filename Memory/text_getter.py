import aiosqlite

#Выбираем сообщение случайным образом
async def get_random():
    try:
        async with aiosqlite.connect('Memory/text.db') as conn:

            res = await conn.execute('SELECT message FROM Messages ORDER BY RANDOM() LIMIT 1')

            msg = await res.fetchone()

            if msg:
                msg = msg[0]
            else:
                print("Сообщения нету")

            return msg
    except Exception as e:
        print(e)

if __name__ == "__main__":

    get_random()
    print("All OK")