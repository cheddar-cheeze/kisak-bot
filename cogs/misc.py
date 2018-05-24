import asyncio
import discord
from discord.ext import commands


class misc():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=True)
    async def info(self, ctx, user: discord.Member=None):
        if user is None:
            embed = discord.Embed(title=ctx.message.author.name + "'s info", description="", color=0xffbc77)
            embed.set_thumbnail(url=ctx.message.author.avatar_url)
            embed.add_field(name="User id", value=ctx.message.author.id, inline=True)
            embed.add_field(name="Server join date", value=ctx.message.author.joined_at, inline=False)
            embed.add_field(name="Discord join date", value=ctx.message.author.created_at.date(), inline=False)
            embed.add_field(name="Status", value=ctx.message.author.status, inline=False)
            await self.bot.say(embed=embed)
        else:
            embed = discord.Embed(title=user.name + "'s info", description="", color=0xffbc77)
            embed.set_thumbnail(url=user.avatar_url)
            embed.add_field(name="User id", value=user.id, inline=True)
            embed.add_field(name="Server join date", value=user.joined_at, inline=False)
            embed.add_field(name="Discord join date", value=user.created_at.date(), inline=False)
            embed.add_field(name="Status", value=user.status, inline=False)
            await self.bot.say(embed=embed)

    @commands.command(pass_context=True, no_pm=True)
    async def server(self, ctx):
        embed = discord.Embed(title="Server info", description="", color=0xffbc77)

    @commands.command(no_pm=True)
    @commands.has_role("جبنة الشيدر")
    async def game(self, *state):
        state = ' '.join(state)
        game = discord.Game(name=state)
        if state == '':
            await self.bot.change_presence(game=None)
        else:
            await self.bot.change_presence(game=game)


def setup(bot):
    bot.add_cog(misc(bot))