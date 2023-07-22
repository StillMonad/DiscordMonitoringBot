from loguru import logger

from src.bot.bot_client import DiscordBotClient
from src.bot.callback_generator import CallbackGenerator

class OnReady(CallbackGenerator):
    async def on_ready(self: DiscordBotClient,):
        logger.info("Logged on as " + str(self.user))
        for g in self.guilds:
            logger.info(f"Connected to: {g.name}, members count is {g.member_count}")