import aiosqlite

async def init_db():
    async with aiosqlite.connect('Memory/text.db') as conn:
        await conn.execute('''CREATE TABLE IF NOT EXISTS Messages(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        message TEXT NOT NULL
        )''')
        await conn.commit()
        print("БД инициализированны")
