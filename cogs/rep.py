import discord
from discord.ext import commands
import asyncio
from utils.database import cursor, connection


class rep():
    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True, no_pm=True)
    async def rep(self, ctx):
        """Rep commands"""

    @rep.command(pass_context=True, no_pm=True)
    @commands.cooldown(1, 86400, commands.BucketType.user)
    async def add(self, ctx, member: discord.Member=None):
        if member is None:
            embed = discord.Embed(title="Command Error!", description="You must mention who to add rep to", color=0xffbc77)
            await self.bot.say(embed=embed)
        else:
            if member is ctx.message.author:
                embed = discord.Embed(title='Command Error!', description="LOL you can't rep your self", color=0xffbc77)
                await self.bot.say(embed=embed)
            else:
                cursor.execute("SELECT rep_val FROM rep WHERE user_id=?", (member.id,))
                data = cursor.fetchone()
                if data is None:
                    cursor.execute("INSERT INTO rep(user_id,rep_val) VALUES(?, 1)", (member.id,))
                    connection.commit()
                    embed = discord.Embed(title="+rep", description=member.mention + " now has 1 rep", color=0xffbc77)
                    await self.bot.say(embed=embed)
                else:
                    value = data[0] + 1
                    cursor.execute("UPDATE rep SET rep_val=? WHERE user_id=?", (value, member.id))
                    connection.commit()
                    embed = discord.Embed(title="+rep", description=member.mention + " now has ``" + str(value) + "`` rep", color=0xffbc77)
                    await self.bot.say(embed=embed)

    @rep.command(pass_context=True, no_pms=True)
    @commands.cooldown(1, 86400, commands.BucketType.user)
    async def subtract(self, ctx, member: discord.Member=None):
        if member is None:
            embed = discord.Embed(title="Command Error!", description="You must mention who to add rep to", color=0xffbc77)
            await self.bot.say(embed=embed)
        else:
            if member is ctx.message.author:
                embed = discord.Embed(title='Command Error!', description="LOL you can't rep your self", color=0xffbc77)
                await self.bot.say(embed=embed)
            else:
                cursor.execute("SELECT rep_val FROM rep WHERE user_id=?", (member.id,))
                data = cursor.fetchone()
                if data is None:
                    cursor.execute("INSERT INTO rep(user_id,rep_val) VALUES(?, -1)", (member.id,))
                    connection.commit()
                    embed = discord.Embed(title="-rep", description=member.mention + " now has -1 rep", color=0xffbc77)
                    await self.bot.say(embed=embed)
                else:
                    value = data[0] - 1
                    cursor.execute("UPDATE rep SET rep_val=? WHERE user_id=?", (value, member.id))
                    connection.commit()
                    embed = discord.Embed(title="-rep", description=member.mention + " now has ``" + str(value) + "`` rep", color=0xffbc77)
                    await self.bot.say(embed=embed)



def setup(bot):
            bot.add_cog(rep(bot))