import discord
from discord.ext import commands
import os
from flask import Flask, jsonify

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)
bot.remove_command("help")

# Load Cogs
cogs = [
    "cogs.general",
    "cogs.moderation",
    "cogs.utility",
    "cogs.ticket",
    "cogs.info"
]

for cog in cogs:
    bot.load_extension(cog)

# Flask Web Panel
app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"status": "Bot is running", "bot_name": bot.user.name})

@app.route("/send/<channel_id>/<message>")
def send_message(channel_id, message):
    channel = bot.get_channel(int(channel_id))
    if channel:
        bot.loop.create_task(channel.send(message))
        return jsonify({"status": "Message sent"})
    return jsonify({"error": "Invalid Channel ID"})

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    await bot.change_presence(activity=discord.Game("Managing Craze Panel!"))
    try:
        synced = await bot.tree.sync()
        print(f"📌 Synced {len(synced)} slash commands!")
    except Exception as e:
        print(f"❌ Sync Error: {e}")

def run_flask():
    app.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    import threading
    threading.Thread(target=run_flask).start()
    bot.run("YOUR_BOT_TOKEN")
