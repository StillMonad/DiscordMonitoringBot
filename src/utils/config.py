import json
import sys


class Config:
    def __init__(self, fname):
        with open(fname, "r") as f:
            data = json.loads(f.read())
            try:
                self.discord_token = data["discord_token"]
                self.discord_guild_id_list = data["discord_guild_id_list"]
                self.notify_telegram = data["notify_telegram"]
                if self.notify_telegram:
                    self.telegram_chat_id_list = data["telegram_chat_id_list"]
                    self.telegram_token = data["telegram_token"]
                    self.messages_time_to_live = data["messages_time_to_live"]
            except KeyError:
                sys.exit("Error reading config file")
