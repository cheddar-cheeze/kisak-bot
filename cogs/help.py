import discord
from discord.ext import commands


class help():
    def __init__(self, bot):
        self.bot = bot

    @commands.group()

def setup(bot):
    bot.add_cog(help(bot))