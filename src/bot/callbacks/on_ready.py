from loguru import logger
from src.bot.base_bot_client import BaseDiscordBotClient


class OnReady:
    async def on_ready(self: BaseDiscordBotClient):
        logger.info("Logged on as " + str(self.user))
        for g in self.guilds:
            logger.info(f"Connected to: {g.name}, members count is {g.member_count}")
