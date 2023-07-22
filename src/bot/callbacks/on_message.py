from loguru import logger

from src.bot.action import Action
from src.bot.callback_generator import CallbackGenerator
from src.bot.bot_client import DiscordBotClient

class OnMessage(CallbackGenerator):
    async def on_message(self: DiscordBotClient, message):
        if message.author == self.user:
            return
        action = Action(
            name=str(message.author),
            guild=message.guild.name,
            channel=message.channel.name,
            action="message",
            message=str(message.content),
        )

        logger.info(action.verbose())
        self.db.add_row(action)