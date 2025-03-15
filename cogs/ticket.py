import discord
from discord import app_commands
from discord.ext import commands

class Ticket(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ticket", description="Create a support ticket")
    async def ticket(self, interaction: discord.Interaction):
        guild = interaction.guild
        category = discord.utils.get(guild.categories, name="Tickets")
        if category is None:
            category = await guild.create_category("Tickets")
        
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(view_channel=False),
            interaction.user: discord.PermissionOverwrite(view_channel=True, send_messages=True)
        }
        ticket_channel = await guild.create_text_channel(f"ticket-{interaction.user.name}", category=category, overwrites=overwrites)
        await ticket_channel.send(f"{interaction.user.mention}, this is your ticket. Please explain your issue.")
        await interaction.response.send_message(f"🎟️ Ticket created: {ticket_channel.mention}", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Ticket(bot))
