from telegram import Bot
from telegram.error import TelegramError


def send_telegram_message(message, token, chat_id):
    """Отправка уведомлений в Telegram"""
    bot = Bot(token=token)
    try:
        bot.send_message(chat_id=chat_id, text=message)
        print("Уведомление отправлено.")
    except TelegramError as e:
        print(f"Ошибка при отправке сообщения: {e}")


# send_telegram_message("Тестовое уведомление", "your_telegram_bot_token", "your_chat_id")
