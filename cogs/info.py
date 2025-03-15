import discord
from discord.ext import commands
from discord import app_commands

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="serverinfo", description="Shows server details")
    async def serverinfo(self, interaction: discord.Interaction):
        guild = interaction.guild
        embed = discord.Embed(title=f"Server Info: {guild.name}", color=discord.Color.blue())
        embed.add_field(name="👥 Members", value=guild.member_count)
        embed.add_field(name="📅 Created On", value=guild.created_at.strftime("%Y-%m-%d"))
        embed.add_field(name="👑 Owner", value=guild.owner)
        embed.set_thumbnail(url=guild.icon.url if guild.icon else None)
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="botinfo", description="Shows bot details")
    async def botinfo(self, interaction: discord.Interaction):
        embed = discord.Embed(title=f"🤖 Bot Info: {self.bot.user.name}", color=discord.Color.green())
        embed.add_field(name="🛠 Commands Loaded", value=len(self.bot.tree.get_commands()))
        embed.add_field(name="📅 Bot Created", value=self.bot.user.created_at.strftime("%Y-%m-%d"))
        embed.set_thumbnail(url=self.bot.user.avatar.url if self.bot.user.avatar else None)
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Info(bot))
