import discord
from discord import app_commands
from discord.ext import commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Check bot's latency")
    async def ping(self, interaction: discord.Interaction):
        latency = round(self.bot.latency * 1000)
        await interaction.response.send_message(f"🏓 Pong! {latency}ms", ephemeral=True)

    @app_commands.command(name="announce", description="Announce a message to everyone")
    async def announce(self, interaction: discord.Interaction, message: str):
        await interaction.channel.send(f"@everyone {message}")
        await interaction.response.send_message("📢 Announcement sent!", ephemeral=True)

async def setup(bot):
    await bot.add_cog(General(bot))
