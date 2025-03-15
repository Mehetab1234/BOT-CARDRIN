import discord
from discord.ext import commands

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="serverinfo")
    async def server_info(self, ctx):
        """Displays server information"""
        guild = ctx.guild
        embed = discord.Embed(title=f"Server Info - {guild.name}", color=discord.Color.blue())
        embed.add_field(name="Owner", value=guild.owner, inline=True)
        embed.add_field(name="Members", value=guild.member_count, inline=True)
        embed.add_field(name="Created At", value=guild.created_at.strftime("%Y-%m-%d"), inline=True)
        await ctx.send(embed=embed)

async def setup(bot):
    if not bot.get_command("serverinfo"):  # Prevent duplicate registration
        await bot.add_cog(Info(bot))
