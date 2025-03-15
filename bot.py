import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from flask import Flask, jsonify
import threading
import asyncio

# Load environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Initialize bot
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# Flask Web App
app = Flask(__name__)

@app.route("/")
def home():
    if bot.user:
        return jsonify({"status": "Bot is running", "bot_name": bot.user.name})
    else:
        return jsonify({"status": "Bot is starting..."}), 503

# Run Flask in a separate thread
def run_flask():
    app.run(host="0.0.0.0", port=5000)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    
    # Start Flask after bot is ready
    threading.Thread(target=run_flask, daemon=True).start()

    # Load all cogs
    await load_cogs()

async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await bot.start(TOKEN)

asyncio.run(main())
