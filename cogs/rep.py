import discord
from discord.ext import commands
from cogs.constants import embed_color, db

cursor = db.cursor()

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
            embed = discord.Embed(title="Command Error!", description="You must mention who to add rep to", color=embed_color)
            await self.bot.say(embed=embed)
        else:
            if member is ctx.message.author:
                embed = discord.Embed(title='Command Error!', description="LOL you can't rep your self", color=embed_color)
                await self.bot.say(embed=embed)
            else:
                cursor.execute("SELECT `value` FROM `rep` WHERE `guild_id`=?, `user_id`=?", (ctx.message.server.id, member.id,))
                data = cursor.fetchone()
                if data is None:
                    cursor.execute("INSERT INTO `rep` (`guild_id`, `user_id`, `value`) VALUES (?, ?, 1)", (ctx.message.server.id, member.id,))
                    db.commit()
                    embed = discord.Embed(title="+rep", description=member.mention + " now has 1 rep", color=embed_color)
                    await self.bot.say(embed=embed)
                else:
                    value = data[0] + 1
                    cursor.execute("UPDATE `rep` SET `value`=? WHERE `guild_id`=?, `user_id`=?", (value, ctx.message.server.id, member.id,))
                    db.commit()
                    embed = discord.Embed(title="+rep", description=member.mention + " now has ``" + str(value) + "`` rep", color=embed_color)
                    await self.bot.say(embed=embed)
        db.close()

    @rep.command(pass_context=True, no_pms=True)
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def subtract(self, ctx, member: discord.Member=None):
        if member is None:
            embed = discord.Embed(title="Command Error!", description="You must mention who to add rep to", color=embed_color)
            await self.bot.say(embed=embed)
        else:
            if member is ctx.message.author:
                embed = discord.Embed(title='Command Error!', description="LOL you can't rep your self", color=embed_color)
                await self.bot.say(embed=embed)
            else:
                cursor.execute("SELECT `value` FROM `rep` WHERE `guild_id`=?, `user_id`=?", (ctx.message.server.id, member.id,))
                data = cursor.fetchone()
                if data is None:
                    cursor.execute("INSERT INTO `rep` (`guild_id`, `user_id`, `value`) VALUES (?, ?, -1)", (ctx.message.server.id, member.id,))
                    db.commit()
                    embed = discord.Embed(title="+rep", description=member.mention + " now has -1 rep", color=embed_color)
                    await self.bot.say(embed=embed)
                else:
                    value = data[0] - 1
                    cursor.execute("UPDATE `rep` SET `value`=? WHERE `guild_id`=?, `user_id`=?", (value, ctx.message.server.id, member.id,))
                    db.commit()
                    embed = discord.Embed(title="+rep", description=member.mention + " now has ``" + str(value) + "`` rep", color=embed_color)
                    await self.bot.say(embed=embed)
        db.close()


def setup(bot):
            bot.add_cog(rep(bot))