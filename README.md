# DiscordMonitoringBot

BOT for logging discord voice chat activity and sending notifications for selected servers via telegram to selected chats

You just need to add your own config.json file to the root:

Example 1:
############ config.json: ############
{
    "discord_token": "<your discord bot token>",
    "discord_guild_id_list": ["<your discord guild id 1>", "<your discord guild id 2>"],
    "notify_telegram": true
    "telegram_token": "<your telegram bot token>",
    "telegram_chat_id_list": ["<your telegtam chat id 1>", "<your telegtam chat id 2>"],
}
######################################
Example 2:
############ config.json: ############
{
    "discord_token": "<your discord bot token>",
    "discord_guild_id_list": ["<your discord guild id 1>", "<your discord guild id 2>"],
    "notify_telegram": false
}
######################################
