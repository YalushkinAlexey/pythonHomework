import asyncio
from bot import bot, dp
import handlers

async def on_startup(_):
    print('I see you!')



# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())