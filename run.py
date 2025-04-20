import asyncio
from src.main import start_app


if __name__ == "__main__":
    bot = start_app()
    asyncio.run(bot.polling())
