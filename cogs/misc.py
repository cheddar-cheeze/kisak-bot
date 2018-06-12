import discord
from discord.ext import commands
import os
from cogs.database import connection, cursor
from cogs.constants import embed_color

class misc():
    def __init__(self, bot):
        self.bot = bot

    async def on_member_join(self, member):
        embed = discord.Embed(title="Member joined!", description="Welcome " + member.mention + ", please read the rules" , color=0xffbc77)
        embed.set_thumbnail(url=member.avatar_url)
        channel = discord.Object(id='429444395721293827')
        await self.bot.send_message(channel, embed=embed)

    async def on_member_remove(self, member):
        embed = discord.Embed(title="Member RQ!!", description=member.mention + " RQ!!", color=0xffbc77)
        embed.set_thumbnail(url=member.avatar_url)
        channel = discord.Object(id='429444395721293827')
        await self.bot.send_message(channel, embed=embed)

    @commands.command(pass_context=True, no_pm=True)
    async def info(self, ctx, user: discord.Member=None):
        if user is None:
            user = ctx.message.author
        cursor.execute("SELECT rep_val FROM rep WHERE user_id=(?)", (user.id,))
        data = cursor.fetchone()
        if data is None:
            cursor.execute("INSERT INTO rep(user_id,rep_val) VALUES(?,0)", (user.id,))
            connection.commit()
            rep = str(0)
        else:
            rep = str(data[0])
        if user is None:
            await self.bot.send_typing(ctx.message.channel)
            embed = discord.Embed(title=ctx.message.author.name + "'s info", description="", color=0xffbc77)
            embed.set_thumbnail(url=ctx.message.author.avatar_url)
            embed.add_field(name="User id", value=ctx.message.author.id)
            embed.add_field(name="Rep", value=rep, inline=True)
            embed.add_field(name="Server join date", value=ctx.message.author.joined_at)
            embed.add_field(name="Discord join date", value=ctx.message.author.created_at.date(), inline=True)
            embed.add_field(name="Status", value=ctx.message.author.status)
            await self.bot.say(embed=embed)
        else:
            await self.bot.send_typing(ctx.message.channel)
            embed = discord.Embed(title=user.name + "'s info", description="", color=0xffbc77)
            embed.set_thumbnail(url=user.avatar_url)
            embed.add_field(name="User id", value=user.id)
            embed.add_field(name="Rep", value=rep, inline=True)
            embed.add_field(name="Server join date", value=user.joined_at)
            embed.add_field(name="Discord join date", value=user.created_at.date(), inline=True)
            embed.add_field(name="Status", value=user.status)
            await self.bot.say(embed=embed)

    @commands.command(pass_context=True, no_pm=True)
    async def server(self, ctx):
        await self.bot.send_typing(ctx.message.channel)
        embed = discord.Embed(title="Server info", description="", color=embed_color)
        embed.set_thumbnail(url=ctx.message.author.server.icon_url)
        embed.add_field(name="Server name", value=ctx.message.author.server.name)
        embed.add_field(name="Server id", value=ctx.message.author.server.id, inline=True)
        embed.add_field(name="Owner", value=ctx.message.author.server.owner.name)
        embed.add_field(name="Server region", value=ctx.message.author.server.region, inline=True)
        embed.add_field(name="Member count", value=ctx.message.author.server.member_count)
        embed.add_field(name="Server creation date", value=ctx.message.author.server.created_at, inline=True)
        embed.add_field(name="Verification level", value=ctx.message.author.server.verification_level)
        embed.add_field(name="Default channel", value=ctx.message.author.server.default_channel, inline=True)
        await self.bot.say(embed=embed)


    @commands.command(pass_context=True, no_pm=True)
    async def unacceptable(self, ctx):
        path = os.getcwd()
        await self.bot.delete_message(ctx.message)
        await self.bot.send_file(destination=ctx.message.channel, fp=path + '/assets/unacceptable.png')

def setup(bot):
    bot.add_cog(misc(bot))