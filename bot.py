import os
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import threading
import asyncio
from web.panel import run_web

# Load environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")
AUTH_LINK = "https://discord.com/oauth2/authorize?client_id=1350449110968176690&permissions=8&scope=bot%20applications.commands"

# Bot setup
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

    # Sync slash commands
    try:
        synced = await bot.tree.sync()
        print(f"✅ Synced {len(synced)} slash commands!")
    except Exception as e:
        print(f"❌ Failed to sync commands: {e}")

    threading.Thread(target=run_web, daemon=True).start()  # Start web panel
    await load_cogs()  # Load all cogs

# Load all cogs
async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await bot.start(TOKEN)

asyncio.run(main())
