import discord
from discord.ext import commands


class raid():
    def __init__(self, bot):
        self.bot = bot

    async def on_member_join(self, member):


def setup(bot):
    bot.add_cog(raid(bot))