import discord
from discord.ext import commands
import os
from flask import Flask
from threading import Thread
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up bot intents
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True  # Required for message commands

# Initialize bot with slash command tree
bot = commands.Bot(command_prefix="!", intents=intents)

# Flask App for Render Port Fix
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_web():
    port = int(os.environ.get("PORT", 5000))  # Render requires a web port
    app.run(host="0.0.0.0", port=port)

# Load all Cogs (Commands from files)
async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user} ({bot.user.id})")
    await load_cogs()  # Load commands
    print("✅ All cogs loaded!")

# Run Flask in a separate thread
Thread(target=run_web).start()

# Run bot with token
bot.run(os.getenv("DISCORD_TOKEN"))
