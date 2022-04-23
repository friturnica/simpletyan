import os
from aiogram import Bot, Dispatcher, executor, types

admin_id = 528190859

bot = Bot(token=os.environ['TOKEN'])
dp = Dispatcher(bot)

def checker(message: types.Message, words: list):
    if "/start" in message.text:
        return True
    
    for word in words:
        if word in message.text.lower():
            return admin_checker(message)
    
    return False

def hello_words_checker(message: types.Message):
    words = [
        "привет",
        "приветик",
        "ку",
        "здарова",
        "qq",
        "кк",
        "прив",
        "привки",
        "приветствую",
    ]

    return checker(message, words)

def morning_words_checker(message: types.Message):
    words = [
        "доброе утро",
        "утро доброе",
        "утречко",
    ]
    return checker(message, words)

def user_checker(message: types.Message):
    return message.from_user.id != admin_id

def admin_checker(message: types.Message):
    return message.from_user.id == admin_id

@dp.message_handler(user_checker, commands=["start"])
async def start_message(message: types.Message):
    await message.reply_animation("https://c.tenor.com/6MxCm3cFTY4AAAAC/siesta-detective.gif", caption="вы не сеня, но вы можете оставить ему скрытое послание!\n\nнапишите всё, что угодно, он не увидит кто написал это:")

@dp.message_handler(hello_words_checker)
async def start_message(message: types.Message):
    await message.answer("приветик!! ❤️")

@dp.message_handler(morning_words_checker)
async def morning_message(message: types.Message):
    await message.reply("доброе утро ❤️💓💗")
    await message.answer("https://vgif.ru/gifs/137/vgif-ru-15282.gif")

@dp.message_handler(admin_checker)
async def all_messages(message: types.Message):
    await message.answer("сень, я тебя не понимаю :(")

@dp.message_handler(user_checker)
async def all_messages(message: types.Message):
    await bot.send_message(admin_id, f"сень, тебе что-то кто-то прислал:\n\n{message.text}")
    await message.answer("сообщение доставлено")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)