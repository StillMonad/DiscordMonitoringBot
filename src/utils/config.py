import json
import sys


class Config:
    def __init__(self, fname):
        with open(fname, "r") as f:
            data = json.loads(f.read())
            try:
                self.discord_token = data["discord_token"]
                self.discord_guild_id = data["discord_guild_id"]
                self.telegram_chat_id_list = data["telegram_chat_id_list"]
                self.telegram_token = data["telegram_token"]
                self.notify_telegram = data["notify_telegram"]
            except KeyError:
                sys.exit("Error reading config file")
