import discord
from discord.ext import commands
from discord import app_commands

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="send", description="Sends a message")
    async def send(self, interaction: discord.Interaction, message: str):
        await interaction.channel.send(message)
        await interaction.response.send_message("✅ Message sent!", ephemeral=True)

    @app_commands.command(name="announce", description="Announces a message")
    async def announce(self, interaction: discord.Interaction, message: str):
        await interaction.channel.send(f"📢 **Announcement:** {message}")
        await interaction.response.send_message("✅ Announcement sent!", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Utility(bot))
