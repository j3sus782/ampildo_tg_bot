from pathlib import Path
from aiogram.types import Message, FSInputFile
from Memory.text_getter import get_random
import random
from gtts import gTTS

async def RND_num():
    rand = random.randint(1,2)
    return rand

async def voice(message: Message):
    rnd = await RND_num()
    if rnd == 1:
        text = await get_random()
    else:
        text = (await get_random()) + (await get_random())

    tts = gTTS(text = text, lang='ru',slow=False)
    file = "Voice_message.ogg"
    path = Path('voice_handlers')/file
    path.parent.mkdir(exist_ok=True)
    tts.save(path)

    ready = FSInputFile(path)
    await message.reply_voice( voice=ready)

if __name__ == "__main__":
    voice()