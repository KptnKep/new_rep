import logging
import asyncio

from aiogram import Dispatcher, Bot
from config_data.config import Config, load_config
from handlers import user_handler, other_handlers
 

# Инициализируем логгер
logger = logging.getLogger(__name__)

async def main():
    
    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')
   
    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')
    
    # Загружаем конфиг в переменную config
    config: Config = load_config()
    
    # Инициализируем бот и диспетчер
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher() 

    #Подключаем роутеры
    dp.include_router(user_handler.router)
    dp.include_router(other_handlers.router)
    
    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
if __name__ =='__main__':
    asyncio.run(main())