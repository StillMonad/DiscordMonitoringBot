import discord

from src.bot.tools.telegram_api_client import TelegramClient
from src.db.activity_log_client import ActivityLogClient
from src.utils.config import Config


class BaseDiscordBotClient(discord.Client):
    config: Config
    db: ActivityLogClient
    telegram_client: TelegramClient
