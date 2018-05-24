import asyncio
import discord
from discord.ext import commands
import os
from utils import config


class misc():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=True)
    async def info(self, ctx, user: discord.Member=None):
        if user is None:
            await self.bot.send_typing(ctx.message.channel)
            embed = discord.Embed(title=ctx.message.author.name + "'s info", description="", color=0xffbc77)
            embed.set_thumbnail(url=ctx.message.author.avatar_url)
            embed.add_field(name="User id", value=ctx.message.author.id, inline=True)
            embed.add_field(name="Server join date", value=ctx.message.author.joined_at, inline=False)
            embed.add_field(name="Discord join date", value=ctx.message.author.created_at.date(), inline=False)
            embed.add_field(name="Status", value=ctx.message.author.status, inline=False)
            await self.bot.say(embed=embed)
        else:
            await self.bot.send_typing(ctx.message.channel)
            embed = discord.Embed(title=user.name + "'s info", description="", color=0xffbc77)
            embed.set_thumbnail(url=user.avatar_url)
            embed.add_field(name="User id", value=user.id, inline=True)
            embed.add_field(name="Server join date", value=user.joined_at, inline=False)
            embed.add_field(name="Discord join date", value=user.created_at.date(), inline=False)
            embed.add_field(name="Status", value=user.status, inline=False)
            await self.bot.say(embed=embed)

    @commands.command(pass_context=True, no_pm=True)
    async def server(self, ctx):
        await self.bot.send_typing(ctx.message.channel)
        embed = discord.Embed(title="Server info", description="", color=0xffbc77)
        embed.set_thumbnail(url=ctx.message.author.server.icon_url)
        embed.add_field(name="Server name", value=ctx.message.author.server.name)
        embed.add_field(name="Server id", value=ctx.message.author.server.id, inline=True)
        embed.add_field(name="Owner", value=ctx.message.author.server.owner.name)
        embed.add_field(name="Server region", value=ctx.message.author.server.region, inline=True)
        embed.add_field(name="Server creation date", value=ctx.message.author.server.created_at)
        embed.add_field(name="Member count", value=ctx.message.author.server.member_count, inline=True)
        embed.add_field(name="Verification level", value=ctx.message.author.server.verification_level)
        embed.add_field(name="Default channel", value=ctx.message.author.server.default_channel, inline=True)
        await self.bot.say(embed=embed)

    @commands.command(pass_context=True, no_pm=True)
    async def game(self, ctx, *state):
        await self.bot.send_typing(ctx.message.channel)
        state = ' '.join(state)
        game = discord.Game(name=state)
        if ctx.message.author.id == config.read('owner-id'):
            if state == '':
                await self.bot.change_presence(game=None)
                embed = discord.Embed(title="Game status", description="Kisak's game has been set to ``None``")
                await self.bot.say(embed=embed)
            else:
                await self.bot.change_presence(game=game)
                embed = discord.Embed(title="Game status", description="Kisak's game status has been set to ``" + game.name + "``", color=0xffbc77)
                await self.bot.say(embed=embed)
        else:
            await self.bot.send_typing(ctx.message.channel)
            embed = discord.Embed(title="Command failed", description="This command may only be executed by the bot owner", color=0xffbc77)
            await self.bot.say(embed=embed)

    @commands.command(pass_context=True, no_pm=True)
    async def unacceptable(self, ctx):
        path = os.getcwd()
        await self.bot.delete_message(ctx.message)
        await self.bot.send_file(destination=ctx.message.channel, fp=path + '/assets/unacceptable.png')


def setup(bot):
    bot.add_cog(misc(bot))