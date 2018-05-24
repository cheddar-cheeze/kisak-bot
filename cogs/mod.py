import asyncio
import discord
from discord.ext import commands
from termcolor import colored
import colorama

class mod():
    def __init__(self, bot):
        self.bot = bot


    @commands.command(pass_context=True, no_pm=True)
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member, *reason):
        reason = ' '.join(reason)
        if reason == "":
            reason = "None was specified"
        embed = discord.Embed(title=user.mention + " was kicked!", description="", color=0xffbc77)
        embed.add_field(name="User id", value=user.id, inline=True)
        embed.add_field(name="Reason", value=reason, inline=False)
        embed.add_field(name="Server join date", value=user.joined_at, inline=False)
        embed.add_field(name="Discord join date", value=user.created_at.date(), inline=False)
        embed.set_thumbnail(url=user.avatar_url)
        await self.bot.say(embed=embed)
        dm = discord.Embed(title="You were kicked from", description=ctx.message.server.name, color=0xffbc77)
        dm.add_field(name="Server id", value=ctx.message.author.server.id, inline=True)
        dm.set_thumbnail(url=ctx.message.server.icon_url)
        dm.add_field(name="Reason", value=reason, inline=False)
        print(colored(user.name + "#" + user.discriminator + " was kicked by " + ctx.message.author.name + "#" + ctx.message.author.discriminator + "\n Reason:" + reason,'red'))
        await self.bot.kick(user)
        await self.bot.send_message(user, embed=dm)


    @commands.command(pass_context=True, no_pm=True)
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member, *reason):
        reason = ' '.join(reason)
        if reason == "":
            reason = "None was specified"
        embed = discord.Embed(title=user.mention + ",was banned!", description="", color=0xffbc77)
        embed.add_field(name="User id", value=user.id, inline=True)
        embed.add_field(name="Reason", value=reason, inline=False)
        embed.add_field(name="Server join date", value=user.joined_at, inline=False)
        embed.add_field(name="Discord join date", value=user.created_at.date(), inline=False)
        embed.set_thumbnail(url=user.avatar_url)
        await self.bot.say(embed=embed)
        dm = discord.Embed(title="You were banned from", description=ctx.message.server.name, color=0xffbc77)
        dm.add_field(name="Server id", value=ctx.message.server.id, inline=True)
        dm.add_field(name="Reason", value=reason, inline=False)
        dm.set_thumbnail(url=ctx.message.server.icon_url)
        print(colored(user.name + "#" + user.discriminator + " was banned by " + ctx.message.author.name + "#" + ctx.message.author.discriminator + "\n Reason:" + reason, 'red'))
        await self.bot.ban(user)
        await self.bot.send_message(user, embed=dm)



def setup(bot):
    bot.add_cog(mod(bot))