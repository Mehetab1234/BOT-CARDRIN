import discord
from discord import app_commands
from discord.ext import commands

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="help", description="Show bot commands")
    async def help(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Bot Commands", description="List of available commands:", color=discord.Color.green())
        embed.add_field(name="General", value="`/ping`, `/announce`", inline=False)
        embed.add_field(name="Moderation", value="`/clear`, `/lock`, `/unlock`", inline=False)
        embed.add_field(name="Utility", value="`/serverinfo`, `/invites`", inline=False)
