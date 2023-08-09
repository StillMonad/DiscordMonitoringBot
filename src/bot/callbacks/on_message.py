from loguru import logger
from src.bot.tools.action import Action
from src.bot.base_bot_client import BaseDiscordBotClient


class OnMessage:
    async def on_message(self: BaseDiscordBotClient, message):
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
