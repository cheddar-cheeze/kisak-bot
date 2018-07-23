import discord
from discord.ext import commands
from cogs.constants import embed_color, db
import traceback
cursor = db.cursor()


class verification():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=True)
    async def verification(self, ctx, role=None):
        try:
            if ctx.message.author.id == ctx.message.server.owner.id:
                cursor.execute("SELECT `enabled`, `role_id` FROM `verification` WHERE `guild_id`=%s", (ctx.message.server.id,))
                data = cursor.fetchone()
                if data is None:
                    for r in ctx.message.server.roles:
                        if r.name == role:
                            r_id = r.id
                    if r_id:
                        cursor.execute("INSERT INTO `verification` (`guild_id`, `role_id`, `enabled`) VALUES (%s, %s, 1)", (ctx.message.server.id, r_id,))
                        db.commit()
                        embed = discord.Embed(title='Verification Enabled', description="", color=0x008000)
                        embed.add_field(name='Verification Role', value=role)
                        await self.bot.say(embed=embed)
                    else:
                        await self.bot.say('this role does not exist')
                else:
                    if role is None:
                        if data['enabled'] == 1:
                            cursor.execute("UPDATE `verification` SET `enabled`=0 WHERE `guild_id`=%s", (ctx.message.server.id,))
                            db.commit()
                            embed = discord.Embed(title='Verification Disabled', description="", color=0x008000)
                            await self.bot.say(embed=embed)
                        if data['enabled'] == 0:
                            cursor.execute("UPDATE `verification` SET `enabled`=1 WHERE `guild_id`=%s", (ctx.message.server.id,))
                            db.commit()
                            embed = discord.Embed(title='Verification Enabled', description="", color=0x008000)
                            embed.add_field(name='Verification Role', value=data['role_id'])
                            await self.bot.say(embed=embed)
                    else:
                        for r in ctx.message.server.roles:
                            if r.name == role:
                                r_id = r.id
                        if r_id:
                            if data['enabled'] == 0:
                                cursor.execute("UPDATE `verification` SET `role_id`=%s, `enabled`=1 WHERE `guild_id`=%s", (r_id, ctx.message.server.id,))
                                db.commit()
                                embed = discord.Embed(title='Verification Enabled', description="", color=0x008000)
                                embed.add_field(name='Verification Role', value=role)
                                await self.bot.say(embed=embed)
                            if data['enabled'] == 1:
                                cursor.execute("UPDATE `verification` SET `role_id`=%s WHERE `guild_id`=%s", (r_id, ctx.message.server.id,))
                                db.commit()
                                embed = discord.Embed(title='Verification Role Changed', description="", color=0x008000)
                                embed.add_field(name='Verification Role', value=role)
                                await self.bot.say(embed=embed)
                        else:
                            await self.bot.say("this role does not exist")
            else:
                embed = discord.Embed(title='Command Error', description='This command may only execute by the server owner', color=0x990000)
                await self.bot.say(embed=embed)
        except:
            embed = discord.Embed(title="An Error Occurred!", description=traceback.format_exc(), color=0x990000)
            await self.bot.say(embed=embed)

    @commands.command(pass_context=True, no_pm=True)
    async def verify(self, ctx, member:discord.Member):
        try:
            if ctx.message.author.server_permissions.manage_roles:
                cursor.execute("SELECT `enabled`, `role_id` FROM `verification` WHERE `guild_id`=%s", (ctx.message.server.id,))
                data = cursor.fetchone()
                if data['enabled'] == 1:
                    await self.bot.add_roles(member, discord.Object(id=data['role_id']))
                    embed = discord.Embed(title='Member Was Verified', description="", color=0x008000)
                    embed.add_field(name='Member', value=member.mention)
                    embed.add_field(name='Whomst Verified Them', value=ctx.message.author.mention, inline=True)
                    embed.set_thumbnail(url=member.avatar_url)
                    await self.bot.say(embed=embed)
                else:
                    embed = discord.Embed(title='Command Error', description='Verification disabled on this server', color=0x990000)
                    await self.bot.say(embed=embed)
        except:
            embed = discord.Embed(title="An Error Occurred!", description=traceback.format_exc(), color=0x990000)
            await self.bot.say(embed=embed)

def setup(bot):
    bot.add_cog(verification(bot))