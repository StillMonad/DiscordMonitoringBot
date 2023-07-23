# DiscordMonitoringBot
## General info
Bot for logging discord voice chat activity and sending notifications via telegram to selected chats.

## Requirements
* python3
* pip

## Setup
### Step 1:

**Unix:**
```
    $ python3 -m venv env
    $ source env/bin/activate
    $ pip install -r requirements.txt
```
**Windows:**
```
    $ python3 -m venv env
    $ .\env\Scripts\activate
    $ pip install -r requirements.txt
```

### Step 2:

Add your own "config.json" file to the project root.
_(messages time to live in seconds: (ttl <= 0) => forever)_:

```
Example 1:
############ config.json: ############
{
    "discord_token": "<your discord bot token>",
    "discord_guild_id_list": ["<your discord guild id 1>", "<your discord guild id 2>"],
    "notify_telegram": true
    "telegram_token": "<your telegram bot token>",
    "telegram_chat_id_list": ["<your telegtam chat id 1>", "<your telegtam chat id 2>"],
    "messages_time_to_live": 3600
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
```
