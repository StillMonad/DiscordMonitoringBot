from loguru import logger

from src.bot.bot_client import DiscordBotClient
from src.bot.callback_generator import CallbackGenerator

class OnDisconnect(CallbackGenerator):
    async def on_disconnect(self: DiscordBotClient,):
        logger.info("Bot disconnected")