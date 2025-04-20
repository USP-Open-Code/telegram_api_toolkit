from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message

from .text import welcome_message, reply_message


def register_handlers(bot: AsyncTeleBot):

    @bot.message_handler(commands=["start"])
    async def start(message: Message):
        await welcome_message(message, bot)

    @bot.message_handler(func=lambda message: True)
    async def reply(message: Message):
        await reply_message(message, bot)

    return bot
