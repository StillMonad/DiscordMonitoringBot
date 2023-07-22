from discord.errors import LoginFailure
from loguru import logger
from src.db.db_client import ActivityLogClient
from src.utils.config import Config
from src.bot.bot_client import DiscordBotClient

if __name__ == "__main__":
    config = Config("config.json")

    logger.info("Initializing database...")
    database = ActivityLogClient()

    try:
        logger.info("Init bot...")
        bot = DiscordBotClient(config)
        logger.info("Starting bot...")
        bot.run(config.discord_token, log_handler=None)
    except LoginFailure:
        print("Failed to login")
