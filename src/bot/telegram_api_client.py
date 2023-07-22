import requests


class TelegramApi:
    def __init__(self, config):
        self.telegram_token = config.telegram_token
        self.telegram_chat_id_list = config.telegram_chat_id_list

    def send_message(self, chat_id, msg):
        msg.replace("#", "")
        params = {
            "chat_id": str(chat_id),
            "text": str(msg),
            "disable_notification": True,
        }
        requests.get(
            f"https://api.telegram.org/bot{self.telegram_token}/sendMessage",
            params=params,
        )

    def broadcast_message(self, msg):
        for chat_id in self.telegram_chat_id_list:
            self.send_message(chat_id, msg)
