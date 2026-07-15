import discord
from discord.ext import commands
from app.config import config
from app.logger import logger

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=config.PREFIX, intents=intents)

@bot.event
async def on_ready():
    logger.info(f\"Discord connected as {bot.user}\")
    print(f\"Online as {bot.user}\")

@bot.command()
async def help(ctx):
    await ctx.send(
\"\"\" 
Hotspot Controller
Commands:
!status
!help
More commands coming.
\"\"\"
    )

@bot.command()
async def status(ctx):
    await ctx.send("?? Raspberry Pi Controller Online")

async def start_bot():
    await bot.start(config.DISCORD_TOKEN)
