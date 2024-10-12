from telebot.async_telebot import AsyncTeleBot
from telebot import TeleBot
import telebot

from src.messages import welcome_message, reply_message

import os


def register_handlers(bot: TeleBot) -> TeleBot:
    """Registra os handlers de mensagens no bot do Telegram.

    Args:
        bot (TeleBot): Instância do bot que será configurada com os handlers.

    Returns:
        TeleBot: A mesma instância do bot, agora com os handlers registrados.
    """
    bot.register_message_handler(welcome_message, content_types=['new_chat_members'], pass_bot=True)
    bot.register_message_handler(reply_message, func=lambda message: True, pass_bot=True)

    return bot


def start_app() -> telebot.async_telebot.AsyncTeleBot:
    """Inicializa e conecta a aplicação ao bot do Telegram.

    A função tenta obter a chave da API do Telegram a partir das variáveis
    de ambiente, inicializa uma instância do bot com `AsyncTeleBot` e registra
    os handlers necessários para gerenciar as interações do bot. Em caso de
    erro, um `ValueError` é levantado com a mensagem de erro apropriada.

    Returns:
        AsyncTeleBot: Instância do bot configurada e pronta para ser executada.

    Raises:
        ValueError: Caso ocorra um erro na leitura da chave da API do Telegram.
    """
    try:
        TELEGRAM_API_KEY = os.environ["TELEGRAM_API_KEY"]
        bot = AsyncTeleBot(TELEGRAM_API_KEY)
        bot = register_handlers(bot)
        return bot
    except ValueError as e:
        raise ValueError(e)
        # usar o logaru para salvar os registros da aplicscao
