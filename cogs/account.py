import json
import discord
from discord.ext import commands
from cogs.constants import embed_color



acc = json.load(open('/home/ubuntu/generator/accounts.cg.json'))

class account():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=True)
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def account(self, ctx):
        await self.bot.delete_message(ctx.message)
        login = acc["array"][1]["login"]
        passwd = acc["array"][1]["password"]
        embed = discord.Embed(title="Account Credentials", color=embed_color)
        embed.add_field(name="Login", value=login)
        embed.add_field(name="Password", value=passwd)
        del acc["array"][1]
        try:
            await self.bot.send_message(ctx.message.author, embed=embed)
        except:
            pass



def setup(bot):
    bot.add_cog(account(bot))