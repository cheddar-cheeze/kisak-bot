import discord
from discord.ext import commands
from cogs.constants import embed_color
from cogs.database import cursor,connection

class spam():
    def __init__(self, bot):
        self.bot = bot
    async def on_message(self, message):
        cursor.execute("SELECT amt,punishment,state FROM mspam WHERE  server_id=?", (message.server.id,))
        mstate = cursor.fetchone()[0]
        amt = cursor.fetchone()[1]
        punish = cursor.fetchone()[2]

        if mstate == 1:
            if len(message.mentions) > amt:
                if punish == 0:
                    """warn"""
                if punish == 1:
                    """mute"""
                if punish == 2:
                    """kick"""
                if punish == 3:
                    """ban"""

    @commands.group(pass_context=True, no_pm=True)
    async def mspam(self, ctx, amt, punish):
        if ctx.message.author == ctx.message.server.owner:
            cursor.execute("INSERT INTO mspam(sever_id,amt,punishment,state) VALUES (?, ?, ?,1)", (ctx.message.author.server.id, amt, punish,))
            connection.commit()

            await self.bot.say(embed=embed)
        else:
            await self.bot.send_typing(ctx.message.channel)
            embed = discord.Embed(title="Command Error!", description="This commands may only be executed by the server owner", color=embed_color)
            await self.bot.say(embed=embed)

    @mspam.command(pass_context=True, no_pm=True)
    async def disable(self, ctx, feature):
        if ctx.message.author == ctx.message.server.owner:
            cursor.execute("INSERT INTO mspam(state) VALUES (?, ?, 1) WHERE", (ctx.message.author.server.id,))
            connection.commit()
        else:
            await self.bot.send_typing(ctx.message.channel)
            embed = discord.Embed(title="Command Error!", description="This commands may only be executed by the server owner", color=embed_color)
            await self.bot.say(embed=embed)



def setup(bot):
    bot.add_cog(spam(bot))
