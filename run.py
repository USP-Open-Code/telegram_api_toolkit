import asyncio
from src import start_app


if __name__ == "__main__":
    bot = start_app()
    asyncio.run(bot.polling())
