import discord
from discord.ext import commands
from discord import app_commands

class Ticket(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ticket", description="Creates a support ticket")
    async def ticket(self, interaction: discord.Interaction):
        overwrites = {
            interaction.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            interaction.user: discord.PermissionOverwrite(read_messages=True, send_messages=True)
        }
        channel = await interaction.guild.create_text_channel(f"ticket-{interaction.user.name}", overwrites=overwrites)
        await interaction.response.send_message(f"✅ Ticket created: {channel.mention}")

async def setup(bot):
    await bot.add_cog(Ticket(bot))
