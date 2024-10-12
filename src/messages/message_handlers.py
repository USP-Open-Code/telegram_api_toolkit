from src.messages.utils import new_chat_inline_keyboard  #, request_llm
from telebot import TeleBot
from telebot.types import Message


async def welcome_message(bot: TeleBot, message: Message):
    """Envia uma mensagem de boas-vindas com um botão de 'START'

    Esta função cria um teclado inline com um botão para que o
    usuário possa iniciar uma interação com o bot.

    Args:
        bot (TeleBot): Instância do bot do TeleBot
        message (Message): Objeto que possui os detalhes da mensagem

    """
    keyboard = new_chat_inline_keyboard()
    await bot.send_message(message.chat.id, reply_markup=keyboard())


async def reply_message(message: Message, bot: TeleBot):
    """Recebe uma mensagem de um usuário, consulta uma API com um LLM e
    retorna uma resposta.

    Esta função processa as interações recebidas dos usuários,
    consultando uma API que utiliza um LLM para gerar uma resposta,
    e então envia uma resposta ao usuário.

    Args:
        bot (TeleBot): Instância do bot do TeleBot
        message (Message): Objeto que possui os detalhes da mensagem
    """
    # llm_response = request_llm(message.text)
    llm_response = "Eu li sua mensagem"
    await bot.reply_to(message, llm_response)
