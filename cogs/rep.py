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
    async def add(self, ctx, user: discord.Member=None):
        if user is None:
            embed = discord.Embed(title="Command Error!", description="You must mention who to add rep to", color=embed_color)
            await self.bot.say(embed=embed)
        else:
            if user is ctx.message.author:
                embed = discord.Embed(title='Command Error!', description="LOL you can't rep your self", color=embed_color)
                await self.bot.say(embed=embed)
            else:
                cursor.execute("SELECT `value` FROM `rep` WHERE `guild_id`=%s AND `user_id`=%s", (ctx.message.server.id, user.id,))
                data = cursor.fetchone()
                if data is None:
                    cursor.execute("INSERT INTO `rep` (`guild_id`, `user_id`, `value`) VALUES (%s, %s, 1)", (ctx.message.server.id, user.id,))
                    db.commit()
                    embed = discord.Embed(title="+rep", description=user.mention + " now has 1 rep", color=embed_color)
                    await self.bot.say(embed=embed)
                else:
                    value = data['value'] + 1
                    cursor.execute("UPDATE `rep` SET `value`=%s WHERE `guild_id`=%s AND`user_id`=%s", (value, ctx.message.server.id, user.id,))
                    db.commit()
                    embed = discord.Embed(title="+rep", description=user.mention + " now has ``" + str(value) + "`` rep", color=embed_color)
                    await self.bot.say(embed=embed)

    @rep.command(pass_context=True, no_pms=True)
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def subtract(self, ctx, user: discord.Member=None):
        if user is None:
            embed = discord.Embed(title="Command Error!", description="You must mention who to add rep to", color=embed_color)
            await self.bot.say(embed=embed)
        else:
            if user is ctx.message.author:
                embed = discord.Embed(title='Command Error!', description="LOL you can't rep your self", color=embed_color)
                await self.bot.say(embed=embed)
            else:
                cursor.execute("SELECT `value` FROM `rep` WHERE `guild_id`=%s AND `user_id`=%s", (ctx.message.server.id, user.id,))
                data = cursor.fetchone()
                if data is None:
                    cursor.execute("INSERT INTO `rep` (`guild_id`, `user_id`, `value`) VALUES (%s, %s, -1)", (ctx.message.server.id, user.id,))
                    db.commit()
                    embed = discord.Embed(title="+rep", description=user.mention + " now has -1 rep", color=embed_color)
                    await self.bot.say(embed=embed)
                else:
                    value = data['value'] - 1
                    cursor.execute("UPDATE `rep` SET `value`=%s WHERE `guild_id`=%s AND`user_id`=%s", (value, ctx.message.server.id, user.id,))
                    db.commit()
                    embed = discord.Embed(title="+rep", description=user.mention + " now has ``" + str(value) + "`` rep", color=embed_color)
                    await self.bot.say(embed=embed)


def setup(bot):
            bot.add_cog(rep(bot))