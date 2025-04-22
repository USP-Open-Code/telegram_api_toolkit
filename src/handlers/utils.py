from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import httpx

from src.settings import settings


async def new_chat_keyboard() -> ReplyKeyboardMarkup:
    """Cria e retorna um teclado inline com um botão 'START'.

    Esta função gera um `ReplyKeyboardMarkup` que contém um único
    botão com o texto 'Start'. O teclado é configurado para redimensionar
    os botões automaticamente com `resize_keyboard=True`.

    Returns:
        ReplyKeyboardMarkup: Um objeto de teclado inline com o botão 'Start'.
    """
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    start_button = KeyboardButton('Start')
    markup.add(start_button)

    return markup


async def request_llm(message: str, user_id: str) -> str:
    """
    Envia uma mensagem para um LLM e retorna a resposta.

    Esta função faz uma requisição POST para um endpoint de API que utiliza
    um modelo de linguagem para processar a mensagem do usuário e gerar uma
    resposta.

    Args:
        message (str): A mensagem enviada pelo usuário.
        user_id (str): Nesse caso, é o telefone da pessoa.

    Returns:
        str: A resposta gerada pelo LLM.
    """
    url = settings.RESPONSE_ENDPOINT
    payload = {
        "message": message,
        "user_id": str(user_id)
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload, timeout=360)
        return response.json().get("response")
