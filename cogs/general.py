import discord
from discord.ext import commands
from discord import app_commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="help", description="Lists all commands")
    async def help_command(self, interaction: discord.Interaction):
        """Displays help message"""
        commands_list = """
        **🔹 Moderation**
        `/clear [amount]` → Deletes messages  
        `/warn [user] [reason]` → Warns a user  

        **🎟 Tickets**
        `/ticket` → Creates a ticket  

        **📢 Extra**
        `/send [message]` → Sends a message  
        `/announce [message]` → Announces a message  

        **🔒 Admin**
        `/lock` → Locks a channel  
        `/unlock` → Unlocks a channel  

        **ℹ️ Info**
        `/serverinfo` → Shows server details  
        `/invites` → Shows user invites  
        `/botinfo` → Shows bot details  
        """
        await interaction.response.send_message(commands_list, ephemeral=True)

    @app_commands.command(name="serverinfo", description="Shows server details")
    async def serverinfo(self, interaction: discord.Interaction):
        """Displays server info"""
        guild = interaction.guild
        embed = discord.Embed(title=f"Server Info: {guild.name}", color=discord.Color.blue())
        embed.add_field(name="👥 Members", value=guild.member_count)
        embed.add_field(name="📅 Created On", value=guild.created_at.strftime("%Y-%m-%d"), inline=False)
        embed.add_field(name="👑 Owner", value=guild.owner, inline=False)
        embed.set_thumbnail(url=guild.icon.url if guild.icon else None)
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="invites", description="Shows user invites")
    async def invites(self, interaction: discord.Interaction, member: discord.Member = None):
        """Shows invite count of a user"""
        member = member or interaction.user
        total_invites = 0
        for invite in await interaction.guild.invites():
            if invite.inviter == member:
                total_invites += invite.uses
        await interaction.response.send_message(f"📨 {member.mention} has **{total_invites}** invites!")

    @app_commands.command(name="botinfo", description="Shows bot details")
    async def botinfo(self, interaction: discord.Interaction):
        """Displays bot info"""
        embed = discord.Embed(title=f"🤖 Bot Info: {self.bot.user.name}", color=discord.Color.green())
        embed.add_field(name="🛠 Commands Loaded", value=len(self.bot.tree.get_commands()))
        embed.add_field(name="📅 Bot Created", value=self.bot.user.created_at.strftime("%Y-%m-%d"), inline=False)
        embed.set_thumbnail(url=self.bot.user.avatar.url if self.bot.user.avatar else None)
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(General(bot))
