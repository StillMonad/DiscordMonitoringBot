from loguru import logger
from src.bot.tools.action import Action
from src.bot.base_bot_client import BaseDiscordBotClient


class OnVoiceStateUpdate:
    async def on_voice_state_update(self: BaseDiscordBotClient, member, before, after):
        if str(member.guild.id) in self.config.discord_guild_id_list:
            member_name = str(member)
            guild_name = str(member.guild)
            state = None

            if before.channel == after.channel:
                channel_name = str(before.channel.name)
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
                if self.config.notify_telegram:
                    self.telegram_client.broadcast_message(action.verbose())
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
                if self.config.notify_telegram:
                    self.telegram_client.broadcast_message(action.verbose())
