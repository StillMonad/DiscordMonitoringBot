from functools import partial

import discord

from src.bot.base_bot_client import BaseDiscordBotClient
from src.db.activity_log_client import ActivityLogClient
from src.bot.tools.telegram_api_client import TelegramClient

from src.bot.callbacks.on_connect import OnConnect
from src.bot.callbacks.on_disconnect import OnDisconnect
from src.bot.callbacks.on_ready import OnReady
from src.bot.callbacks.on_message import OnMessage
from src.bot.callbacks.on_voice_state_update import OnVoiceStateUpdate


class DiscordBotClient(BaseDiscordBotClient):
    def __init__(self, config):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)

        self.config = config
        if self.config.notify_telegram is True:
            self.telegram_client = TelegramClient(config)
        self.db = ActivityLogClient()

        if config.messages_time_to_live > 0:
            self.telegram_client.start_polling_daemon()

        self.on_connect = partial(OnConnect.on_connect, self)
        self.on_disconnect = partial(OnDisconnect.on_disconnect, self)
        self.on_ready = partial(OnReady.on_ready, self)
        self.on_message = partial(OnMessage.on_message, self)
        self.on_voice_state_update = partial(
            OnVoiceStateUpdate.on_voice_state_update, self
        )
