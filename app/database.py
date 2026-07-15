import aiosqlite
from app.config import config

async def init_database():
    async with aiosqlite.connect(config.DATABASE) as db:
        await db.execute(
            \"
            CREATE TABLE IF NOT EXISTS hotspots
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                bandwidth TEXT DEFAULT 'unlimited',
                max_clients INTEGER DEFAULT 10,
                enabled INTEGER DEFAULT 1,
                created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            \"
        )
        await db.execute(
            \"
            CREATE TABLE IF NOT EXISTS errors
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                message TEXT,
                created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            \"
        )
        await db.commit()
