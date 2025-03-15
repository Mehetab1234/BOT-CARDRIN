import discord
from discord import app_commands
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.warnings = {}  # Dictionary to store user warnings

    @app_commands.command(name="clear", description="Clear messages in a channel")
    @app_commands.checks.has_permissions(manage_messages=True)
    async def clear(self, interaction: discord.Interaction, amount: int):
        await interaction.channel.purge(limit=amount)
        await interaction.response.send_message(f"🧹 Cleared {amount} messages.", ephemeral=True)

    @app_commands.command(name="lock", description="Lock a channel")
    @app_commands.checks.has_permissions(manage_channels=True)
    async def lock(self, interaction: discord.Interaction):
        await interaction.channel.set_permissions(interaction.guild.default_role, send_messages=False)
        await interaction.response.send_message("🔒 Channel locked!", ephemeral=True)

    @app_commands.command(name="unlock", description="Unlock a channel")
    @app_commands.checks.has_permissions(manage_channels=True)
    async def unlock(self, interaction: discord.Interaction):
        await interaction.channel.set_permissions(interaction.guild.default_role, send_messages=True)
        await interaction.response.send_message("🔓 Channel unlocked!", ephemeral=True)

    @app_commands.command(name="warn", description="Warn a user")
    @app_commands.checks.has_permissions(manage_messages=True)
    async def warn(self, interaction: discord.Interaction, member: discord.Member, reason: str = "No reason provided"):
        if member.id not in self.warnings:
            self.warnings[member.id] = []
        self.warnings[member.id].append(reason)
        await interaction.response.send_message(f"⚠️ {member.mention} has been warned for: {reason}")

    @app_commands.command(name="warnings", description="Check a user's warnings")
    async def warnings(self, interaction: discord.Interaction, member: discord.Member):
        user_warnings = self.warnings.get(member.id, [])
        if not user_warnings:
            await interaction.response.send_message(f"✅ {member.mention} has no warnings.")
        else:
            warnings_list = "\n".join([f"{i+1}. {w}" for i, w in enumerate(user_warnings)])
            await interaction.response.send_message(f"⚠️ {member.mention} has **{len(user_warnings)}** warnings:\n{warnings_list}")

async def setup(bot):
    await bot.add_cog(Moderation(bot))
