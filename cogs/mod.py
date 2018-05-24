import asyncio
import discord
from discord.ext import commands
from termcolor import colored
import colorama
from utils import config

class mod():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=True)
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member, *reason):
        reason = ' '.join(reason)
        if reason == "":
            reason = "None was specified"
        await self.bot.send_typing(ctx.message.channel)
        embed = discord.Embed(title=user.name + " was kicked!", description="", color=0xffbc77)
        embed.add_field(name="User id", value=user.id, inline=True)
        embed.add_field(name="Reason", value=reason, inline=False)
        embed.add_field(name="Server join date", value=user.joined_at, inline=False)
        embed.add_field(name="Discord join date", value=user.created_at.date(), inline=False)
        embed.set_thumbnail(url=user.avatar_url)
        await self.bot.say(embed=embed)
        odm = discord.Embed(title="A member was kicked from your server", description="", color=0xffbc77)
        odm.add_field(name="Server Name", value=ctx.message.server.name)
        odm.add_field(name="Server id", value=ctx.message.server.id, inline=True)
        odm.add_field(name="Member name", value=user.name)
        odm.add_field(name="Member id", value=user.id, inline=True)
        odm.add_field(name="Who kicked them", value=ctx.message.author)
        odm.add_field(name="Reason", value=reason, inline=True)
        odm.set_thumbnail(url=user.avatar_url)
        await self.bot.send_message(ctx.message.server.owner, embed=odm)
        dm = discord.Embed(title="You were kicked from a server", description="", color=0xffbc77)
        dm.set_thumbnail(url=ctx.message.server.icon_url)
        dm.add_field(name="Server name", value=ctx.message.server.name)
        dm.add_field(name="Server id", value=ctx.message.server.id, inline=True)
        dm.add_field(name="Reason", value=reason)
        print(colored(user + " was kicked by " + ctx.message.author + "\n Reason:" + reason, 'red'))
        await self.bot.send_message(user, embed=dm)
        await self.bot.kick(user)


    @commands.command(pass_context=True, no_pm=True)
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member, *reason):
        reason = ' '.join(reason)
        if reason == "":
            reason = "None was specified"
        await self.bot.send_typing(ctx.message.channel)
        embed = discord.Embed(title=user.name + ",was banned!", description="", color=0xffbc77)
        embed.add_field(name="User id", value=user.id, inline=True)
        embed.add_field(name="Reason", value=reason, inline=False)
        embed.add_field(name="Server join date", value=user.joined_at, inline=False)
        embed.add_field(name="Discord join date", value=user.created_at.date(), inline=False)
        embed.set_thumbnail(url=user.avatar_url)
        await self.bot.say(embed=embed)
        odm = discord.Embed(title="A member was banned from your server", description="", color=0xffbc77)
        odm.add_field(name="Server Name", value=ctx.message.server.name)
        odm.add_field(name="Server id", value=ctx.message.server.id, inline=True)
        odm.add_field(name="Member name", value=user.name)
        odm.add_field(name="Member id", value=user.id, inline=True)
        odm.add_field(name="Who banned them", value=ctx.message.author)
        odm.add_field(name="Reason", value=reason, inline=True)
        odm.set_thumbnail(url=user.avatar_url)
        await self.bot.send_message(ctx.message.server.owner, embed=odm)
        dm = discord.Embed(title="You were banned from a server", description="", color=0xffbc77)
        dm.add_field(name="Server name", value=ctx.message.server.name)
        dm.add_field(name="Server id", value=ctx.message.server.id, inline=True)
        dm.add_field(name="Reason", value=reason)
        dm.set_thumbnail(url=ctx.message.server.icon_url)
        print(colored(user + " was banned by " + ctx.message.author + "\n Reason:" + reason, 'red'))
        await self.bot.send_message(user, embed=dm)
        await self.bot.ban(user)



def setup(bot):
    bot.add_cog(mod(bot))