from loguru import logger

from src.bot.base_bot_client import BaseDiscordBotClient


class OnConnect:
    async def on_connect(self: BaseDiscordBotClient):
        logger.info("Bot connected")
