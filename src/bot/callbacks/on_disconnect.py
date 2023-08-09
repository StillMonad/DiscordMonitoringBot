from loguru import logger

from src.bot.base_bot_client import BaseDiscordBotClient


class OnDisconnect:
    async def on_disconnect(self: BaseDiscordBotClient):
        logger.info("Bot disconnected")
