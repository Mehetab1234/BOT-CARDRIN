import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Bot setup with intents
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)

# Auto-load cogs
async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

# Event: Bot is ready
@bot.event
async def on_ready():
    await load_cogs()
    print(f"✅ Bot is online as {bot.user}")

# Error handling for commands
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("🚫 You don't have permission to use this command!", delete_after=5)
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("⚠️ Missing required argument!", delete_after=5)
    else:
        await ctx.send(f"❌ An error occurred: {error}")

# Run bot
bot.run(TOKEN)
