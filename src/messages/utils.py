import requests
from telebot.types import ReplyKeyboardMarkup, KeyboardButton


# def request_llm(message) -> str:
#     response = requests(message)
#     return response

def new_chat_inline_keyboard() -> ReplyKeyboardMarkup:
    """Cria e retorna um teclado inline com um botão 'START'.

    Esta função gera um `ReplyKeyboardMarkup` que contém um único botão com o texto 'Start'. 
    O teclado é configurado para redimensionar os botões automaticamente com `resize_keyboard=True`.

    Returns:
        ReplyKeyboardMarkup: Um objeto de teclado inline com o botão 'Start'.
    """
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    start_button = KeyboardButton('Start')
    markup.add(start_button)

    return markup
