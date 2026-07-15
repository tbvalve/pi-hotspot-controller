import asyncio
from app.database import init_database
from app.discord_bot import start_bot
from app.logger import logger

async def main():
    logger.info(\"Starting controller\")
    await init_database()
    await start_bot()

if __name__ == \"__main__\":
    asyncio.run(main())
