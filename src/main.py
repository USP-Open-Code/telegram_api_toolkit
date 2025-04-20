from telebot.async_telebot import AsyncTeleBot
import telebot

from src.handlers import register_handlers
from src.settings import settings


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
        TELEGRAM_KEY = settings.TELEGRAM_KEY
        bot = AsyncTeleBot(TELEGRAM_KEY)
        bot = register_handlers(bot)
        return bot
    except ValueError as e:
        raise ValueError(e)
