import discord

from src.db.db_client import ActivityLogClient
from src.bot.telegram_api_client import TelegramClient
from src.bot.callback_generator import CallbackGenerator


class DiscordBotClient(discord.Client):
    def __init__(self, config):
        CallbackGenerator.bind(self)

        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)

        self.config = config
        if self.config.notify_telegram is True:
            self.telegram_api_client = TelegramClient(config)
        self.db = ActivityLogClient()

        if config.messages_time_to_live > 0:
            self.telegram_api_client.start_polling_daemon()
