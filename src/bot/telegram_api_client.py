import time

import requests
import threading
from loguru import logger


class TelegramClient:
    class Message:
        def __init__(self, chat_id, message_id, time_to_live):
            self.chat_id = chat_id
            self.message_id = message_id
            self.time_to_live = time_to_live

    def __init__(self, config):
        self.telegram_token = config.telegram_token
        self.telegram_chat_id_list = config.telegram_chat_id_list
        self.messages_time_to_live = config.messages_time_to_live

        self.sent_messages: list[TelegramClient.Message] = []

        self.__is_polling = False
        self.__polling_cycle = 5

    def start_polling_daemon(self):
        self.__is_polling = True
        logger.info("Starting message_timeout_daemon garbage collector")
        threading.Thread(
            target=self.__loop, daemon=True, name="message_timeout_daemon"
        ).start()

    def __loop(self):
        logger.info("Started message_timeout_daemon")
        time_prev = time.time()
        while self.__is_polling:
            time_now = time.time()
            time_diff = time_now - time_prev
            for i in range(len(self.sent_messages)):
                m = self.sent_messages[i]
                m.time_to_live -= time_diff
                if m.time_to_live <= 0:
                    self.delete_message(m.chat_id, m.message_id)
                    self.sent_messages.pop(i)
            time_prev = time_now
            time.sleep(self.__polling_cycle)

    def send_message(self, chat_id, msg, ttl=60):
        msg.replace("#", "")
        params = {
            "chat_id": str(chat_id),
            "text": str(msg),
            "disable_notification": True,
        }

        logger.info(f"sending to chat_id: {chat_id}, message_text: {msg}")
        resp = requests.get(
            f"https://api.telegram.org/bot{self.telegram_token}/sendMessage",
            params=params,
        )
        message_id = resp.json()["result"]["message_id"]
        self.sent_messages.append(
            TelegramClient.Message(chat_id, message_id, self.messages_time_to_live)
        )

        return resp

    def broadcast_message(self, msg):
        out = []
        for chat_id in self.telegram_chat_id_list:
            out.append(self.send_message(chat_id, msg))
        return out

    def delete_message(self, chat_id, message_id):
        params = {"chat_id": str(chat_id), "message_id": str(message_id)}

        logger.info(f"deleting chat_id: {chat_id}, message_id: {message_id}")
        return requests.post(
            f"https://api.telegram.org/bot{self.telegram_token}/deleteMessage",
            params=params,
        )

    def broadcast_message_delete(self, msg_ids):
        out = []
        for i in range(len(self.telegram_chat_id_list)):
            out.append(self.delete_message(self.telegram_chat_id_list[i], msg_ids[i]))
        return out
