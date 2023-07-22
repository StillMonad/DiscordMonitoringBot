from loguru import logger

from src.bot.bot_client import DiscordBotClient
from src.bot.callback_generator import CallbackGenerator

class OnConnect(CallbackGenerator):
    async def on_connect(self: DiscordBotClient,):
        logger.info("Bot connected")