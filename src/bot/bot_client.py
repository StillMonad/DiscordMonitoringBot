import discord

from src.db.db_client import ActivityLogClient
from src.bot.telegram_api_client import TelegramApi
from src.bot.callback_generator import CallbackGenerator

class DiscordBotClient(discord.Client):
    def __init__(self, config):
        CallbackGenerator.bind(self)

        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)

        self.config = config
        if self.config.notify_telegram == True:
            self.telegram_api_client = TelegramApi(config)
        self.db = ActivityLogClient()
