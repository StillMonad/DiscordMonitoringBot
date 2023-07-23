import telebot
from telebot.types import Message

from src.utils.config import Config

# run this bot and type /id to get chat id for "config.json"'s "telegram_chat_id_list"

if __name__ == "__main__":
    bot = telebot.TeleBot(Config("config.json").telegram_token)

    @bot.message_handler(commands=["id"])
    def echo_message(message: Message):
        repl = "Chat ID: " + str(message.chat.id) + "\n"
        repl += "User ID: " + str(message.from_user.id) + "\n"
        bot.send_message(message.chat.id, repl, disable_notification=True)
        bot.delete_message()

    bot.infinity_polling()
