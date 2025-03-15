import discord
from discord.ext import commands
from discord import app_commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Clear messages (!clear)
    @commands.command(name="clear")
    async def clear(self, ctx, amount: int):
        """Deletes messages"""
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f"🗑 Deleted {amount} messages!", delete_after=3)

    # Slash command /clear
    @app_commands.command(name="clear", description="Deletes messages")
    async def clear_slash(self, interaction: discord.Interaction, amount: int):
        """Deletes messages (slash command)"""
        await interaction.channel.purge(limit=amount + 1)
        await interaction.response.send_message(f"🗑 Deleted {amount} messages!", ephemeral=True)

    # Warn command (!warn)
    @commands.command(name="warn")
    async def warn(self, ctx, member: discord.Member, *, reason: str):
        """Warns a user"""
        await ctx.send(f"⚠️ {member.mention} has been warned for: {reason}")

    # Slash warn command (/warn)
    @app_commands.command(name="warn", description="Warn a user")
    async def warn_slash(self, interaction: discord.Interaction, member: discord.Member, reason: str):
        """Warns a user (slash command)"""
        await interaction.response.send_message(f"⚠️ {member.mention} has been warned for: {reason}")

async def setup(bot):
    await bot.add_cog(Moderation(bot))
