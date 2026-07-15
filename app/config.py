import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
    OWNER_ID = int(os.getenv("OWNER_ID", "0"))
    PREFIX = os.getenv("BOT_PREFIX", "!")
    DATABASE = os.getenv("DATABASE_PATH", "database/hotspot.db")
    LOG_FILE = os.getenv("LOG_PATH", "logs/controller.log")

config = Config()
