import json
import discord
from discord.ext import commands
from cogs.constants import embed_color


path = '/home/ubuntu/generator/accounts.cg.json'

class account():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=True)
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def account(self, ctx):
        """sends a direct message with credentials for a steam account"""
        with open(path, 'r+') as json_file:
            out = json.load(json_file)
            login = out["array"][1]["login"]
            passwd = out["array"][1]["password"]
            del out["array"][1]
            used = out["used"]
            out["used"] = used + 1
            json_file.seek(0)
            json_file.write(json.dumps(out))
            json_file.truncate()
            json_file.close()
        try:
            await self.bot.delete_message(ctx.message)
        except:
            pass
        embed = discord.Embed(title="Steam Account Credentials", color=embed_color)
        embed.add_field(name="Login", value=login)
        embed.add_field(name="Password", value=passwd)
        try:
            await self.bot.send_message(ctx.message.author, embed=embed)
        except:
            pass

    @commands.command(pass_context=True, no_pm=True)
    async def geninfo(self, ctx):
        with open(path, 'r') as json_file:
            out = json.load(json_file)
            used = out["used"]
            amt = len(out["array"])
            json_file.close()
        embed = discord.Embed(title="Steam Account Generator Info", color=embed_color)
        embed.add_field(name='Steam Accounts Available', value=str(amt) + " accounts")
        embed.add_field(name='Steam Accounts Used', value=str(used) + " accounts", inline=True)
        await self.bot.say(embed=embed)



def setup(bot):
    bot.add_cog(account(bot))