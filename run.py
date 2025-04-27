import asyncio
from src.main import start_app


if __name__ == "__main__":
    bot = start_app()
    print(f"{30*'-'}Bot started{30*'-'}")
    asyncio.run(bot.polling())
