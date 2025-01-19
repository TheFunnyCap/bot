import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="7677566905:AAHPvcCEQ7VRJVHlESuSiufzK60MIVOUW6c")
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Ну здарова!")

@dp.message()  # Создаём новое событие, которое запускается в ответ на любой текст, введённый пользователем 
async def echo(message: types.Message):  # Создаём функцию с простой задачей — отправить обратно тот же текст, что ввёл пользователь 
    await message.answer(message.text)

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
