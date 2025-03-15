import discord
from discord import app_commands
from discord.ext import commands

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="serverinfo", description="Get server info")
    async def serverinfo(self, interaction: discord.Interaction):
        guild = interaction.guild
        embed = discord.Embed(title=guild.name, description=f"ID: {guild.id}", color=discord.Color.blue())
        embed.set_thumbnail(url=guild.icon.url if guild.icon else None)
        embed.add_field(name="Members", value=guild.member_count)
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="invites", description="Show server invite statistics")
    async def invites(self, interaction: discord.Interaction, member: discord.Member = None):
        if member is None:
            member = interaction.user
        total_invites = sum(i.uses for i in await interaction.guild.invites() if i.inviter == member)
        await interaction.response.send_message(f"📨 {member.mention} has **{total_invites}** invites.")

async def setup(bot):
    await bot.add_cog(Utility(bot))
