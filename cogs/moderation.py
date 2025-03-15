import discord
from discord.ext import commands
from discord import app_commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="clear", description="Deletes messages")
    async def clear(self, interaction: discord.Interaction, amount: int):
        await interaction.channel.purge(limit=amount + 1)
        await interaction.response.send_message(f"✅ Deleted {amount} messages!", ephemeral=True)

    @app_commands.command(name="warn", description="Warns a user")
    async def warn(self, interaction: discord.Interaction, user: discord.Member, reason: str):
        await interaction.response.send_message(f"⚠️ {user.mention} has been warned for: {reason}")

    @app_commands.command(name="lock", description="Locks a channel")
    async def lock(self, interaction: discord.Interaction):
        await interaction.channel.set_permissions(interaction.guild.default_role, send_messages=False)
        await interaction.response.send_message("🔒 Channel locked!")

    @app_commands.command(name="unlock", description="Unlocks a channel")
    async def unlock(self, interaction: discord.Interaction):
        await interaction.channel.set_permissions(interaction.guild.default_role, send_messages=True)
        await interaction.response.send_message("🔓 Channel unlocked!")

async def setup(bot):
    await bot.add_cog(Moderation(bot))
