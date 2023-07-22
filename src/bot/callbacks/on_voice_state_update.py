from loguru import logger

from src.bot.action import Action
from src.bot.bot_client import DiscordBotClient
from src.bot.callback_generator import CallbackGenerator

class OnVoiceStateUpdate(CallbackGenerator):
    async def on_voice_state_update(self: DiscordBotClient, member, before, after):
        if str(member.guild.id) == self.config.discord_guild_id:
            member_name = str(member)
            guild_name = str(member.guild)

            state = await self.get_user_state(member, before, after)
            if state is not None:
                return

            if after.channel is None:
                channel_name = str(before.channel.name)
                action = Action(
                    name=member_name,
                    guild=guild_name,
                    channel=channel_name,
                    action="left",
                    message="",
                )
                logger.info(action.verbose())
                self.db.add_row(action)
                if self.config.notify_telegram == True:
                    self.telegram_api_client.broadcast_message(action.verbose())
            if after.channel is not None:
                channel_name = str(after.channel.name)
                action = Action(
                    name=member_name,
                    guild=guild_name,
                    channel=channel_name,
                    action="joined",
                    message="",
                )
                logger.info(action.verbose())
                self.db.add_row(action)
                if self.config.notify_telegram == True:
                    self.telegram_api_client.broadcast_message(action.verbose())

    async def get_user_state(self, member, before, after):
        member_name = str(member)
        guild_name = str(member.guild)
        if before.channel == after.channel:
            channel_name = str(before.channel.name)
            state = "unknown"
            if before.self_deaf != after.self_deaf:
                if after.self_deaf:
                    state = "deafened"
                elif not after.self_deaf:
                    state = "undeafened"
            elif before.self_mute != after.self_mute:
                if after.self_mute:
                    state = "muted"
                elif not after.self_mute:
                    state = "unmuted"

            action = Action(
                name=member_name,
                guild=guild_name,
                channel=channel_name,
                action=state,
                message="",
            )
            logger.info(action.verbose())
            self.db.add_row(action)
            return state