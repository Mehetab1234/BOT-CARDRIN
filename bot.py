import os
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
from flask import Flask, jsonify
import threading
import asyncio

# Load environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")
AUTH_LINK = "https://discord.com/oauth2/authorize?client_id=1350449110968176690"

# Bot setup
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# Flask Web Panel
app = Flask(__name__)

@app.route("/")
def home():
    if bot.user:
        return jsonify({
            "status": "Bot is running",
            "bot_name": bot.user.name,
            "auth_link": AUTH_LINK
        })
    else:
        return jsonify({"status": "Bot is starting..."}), 503

# Run Flask in a separate thread
def run_flask():
    app.run(host="0.0.0.0", port=5000)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    threading.Thread(target=run_flask, daemon=True).start()

    try:
        synced = await bot.tree.sync()  # Sync slash commands
        print(f"✅ Synced {len(synced)} commands!")
    except Exception as e:
        print(f"❌ Failed to sync commands: {e}")

    await load_cogs()

async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await bot.start(TOKEN)

asyncio.run(main())
