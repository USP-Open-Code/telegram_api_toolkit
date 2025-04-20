from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message

from src.handlers.utils import new_chat_keyboard, request_llm


async def welcome_message(message: Message, bot: AsyncTeleBot):
    """Envia uma mensagem de boas-vindas com um botão de 'START'

    Esta função cria um teclado inline com um botão para que o
    usuário possa iniciar uma interação com o bot.

    Args:
        message (Message): Objeto que possui os detalhes da mensagem
        bot (AsyncTeleBot): Instância do bot do TeleBot

    """
    keyboard = new_chat_keyboard()
    await bot.send_message(message.chat.id, reply_markup=keyboard())


async def reply_message(message: Message, bot: AsyncTeleBot) -> None:
    """
    consulta uma API com um LLM e retorna uma resposta.

    Args:
        message (Message): Objeto que possui os detalhes da mensagem
        bot (AsyncTeleBot): Instância do bot do TeleBot

    """
    try:
        response = await request_llm(message.text, message.from_user.id)
        await bot.send_message(message.chat.id, response)
    except Exception:
        await bot.send_message(
            message.chat.id,
            "Erro ao processar a mensagem. Tente novamente mais tarde."
        )
