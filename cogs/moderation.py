import discord
from discord.ext import commands
from discord import app_commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # 🧹 Clear Messages Command
    @app_commands.command(name="clear", description="Clear a number of messages in this channel.")
    @app_commands.checks.has_permissions(manage_messages=True)
    async def clear(self, interaction: discord.Interaction, amount: int):
        await interaction.channel.purge(limit=amount)
        await interaction.response.send_message(f"✅ Cleared {amount} messages!", ephemeral=True)

    # 🔒 Lock Channel Command
    @app_commands.command(name="lock", description="Lock the current channel.")
    @app_commands.checks.has_permissions(manage_channels=True)
    async def lock(self, interaction: discord.Interaction):
        overwrite = interaction.channel.overwrites_for(interaction.guild.default_role)
        overwrite.send_messages = False
        await interaction.channel.set_permissions(interaction.guild.default_role, overwrite=overwrite)
        await interaction.response.send_message("🔒 This channel has been locked!", ephemeral=True)

    # 🔓 Unlock Channel Command
    @app_commands.command(name="unlock", description="Unlock the current channel.")
    @app_commands.checks.has_permissions(manage_channels=True)
    async def unlock(self, interaction: discord.Interaction):
        overwrite = interaction.channel.overwrites_for(interaction.guild.default_role)
        overwrite.send_messages = True
        await interaction.channel.set_permissions(interaction.guild.default_role, overwrite=overwrite)
        await interaction.response.send_message("🔓 This channel has been unlocked!", ephemeral=True)

    # ⚠️ Warn User Command
    @app_commands.command(name="warn", description="Warn a user for bad behavior.")
    @app_commands.checks.has_permissions(manage_messages=True)
    async def warn(self, interaction: discord.Interaction, member: discord.Member, reason: str):
        await member.send(f"⚠️ You have been warned for: {reason}")
        await interaction.response.send_message(f"✅ Warned {member.mention} for: {reason}", ephemeral=True)

    # 📜 View Warnings Command
    warnings = {}

    @app_commands.command(name="warnings", description="Check a user's warnings.")
    async def warnings(self, interaction: discord.Interaction, member: discord.Member):
        count = self.warnings.get(member.id, 0)
        await interaction.response.send_message(f"⚠️ {member.mention} has {count} warnings.", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Moderation(bot))
