import discord
from discord.ext import commands
import time
import calendar
import traceback
from cogs.constants import db
cursor = db.cursor()

class auto_mod():
    def __init__(self, bot):
        self.bot = bot
    async def on_member_join(self, member):
        cursor.execute("SELECT `enabled`, `role_id` FROM `verification` WHERE `guild_id`=%s", (member.server.id,))
        datax = cursor.fetchone()
        cursor.execute("SELECT * FROM `auto_verify` WHERE `guild_id`=%s", (member.server.id,))
        datay = cursor.fetchone()
        if datax['enabled'] == 1:
            if datay['enabled'] == 1:
                year  = member.created_at.year
                month = member.created_at.month
                day =  member.created_at.day
                hour = member.created_at.hour
                min = member.created_at.minute
                sec = member.created_at.second
                member_epoch = calendar.timegm((int(year), int(month), int(day), int(hour), int(min), int(sec)))
                if member.avatar:
                    avatar = 1
                else:
                    avatar = 0
                if member.status != discord.Status.offline:
                    online = 1
                else:
                    online = 0
                if datay['avatar_req'] <= avatar:
                    if datay['online_req'] <= online:
                        if datay['date_req'] == 0:
                            await self.bot.add_roles(member, discord.Object(id=datax['role_id']))
                            embed = discord.Embed(title="Auto-Verification",
                                                  description="You have met the requirements to be auto-verified in the following server",
                                                  color=0x008000)
                            embed.add_field(name="Server Name", value=member.server.name)
                            embed.add_field(name="Server Id", value=member.server.id, inline=True)
                            await self.bot.send_message(member, embed=embed)
                        else:
                            if member_epoch < int(time.time()) - datay['date_req']:
                                await self.bot.add_roles(member, discord.Object(id=datax['role_id']))
                                embed = discord.Embed(title="Auto-Verification",
                                                      description="You have met the requirements to be auto-verified in the following server",
                                                      color=0x008000)
                                embed.add_field(name="Server Name", value=member.server.name)
                                embed.add_field(name="Server Id", value=member.server.id, inline=True)
                                await self.bot.send_message(member, embed=embed)
                            else:
                                embed = discord.Embed(title="Auto-Verification",
                                                      description="You have not met the requirements to be auto-verified in the following server; please wait for an admin to verify you",
                                                      color=0x990000)
                                embed.add_field(name="Server Name", value=member.server.name)
                                embed.add_field(name="Server Id", value=member.server.id, inline=True)
                                await self.bot.send_message(member, embed=embed)
                    else:
                        if datay['date_req'] == 0:
                            await self.bot.add_roles(member, discord.Object(id=datax['role_id']))
                            embed =discord.Embed(title="Auto-Verification", description="You have met the requirements to be auto-verified in the following server", color=0x008000)
                            embed.add_field(name="Server Name", value=member.server.name)
                            embed.add_field(name="Server Id", value=member.server.id, inline=True)
                            await self.bot.send_message(member, embed=embed)
                        else:
                            if member_epoch < int(time.time()) - datay['date_req']:
                                await self.bot.add_roles(member, discord.Object(id=datax['role_id']))
                                embed = discord.Embed(title="Auto-Verification", description="You have met the requirements to be auto-verified in the following server", color=0x008000)
                                embed.add_field(name="Server Name", value=member.server.name)
                                embed.add_field(name="Server Id", value=member.server.id, inline=True)
                                await self.bot.send_message(member, embed=embed)
                            else:
                                embed = discord.Embed(title="Auto-Verification", description="You have not met the requirements to be auto-verified in the following server; please wait for an admin to verify you", color=0x990000)
                                embed.add_field(name="Server Name", value=member.server.name)
                                embed.add_field(name="Server Id", value=member.server.id, inline=True)
                                await self.bot.send_message(member, embed=embed)
                else:
                    embed = discord.Embed(title="Auto-Verification", description="You have not met the requirements to be auto-verified in the following server; please wait for an admin to verify you", color=0x990000)
                    embed.add_field(name="Server Name", value=member.server.name)
                    embed.add_field(name="Server Id", value=member.server.id, inline=True)
                    await self.bot.send_message(member, embed=embed)

    @commands.command(pass_context=True)
    async def autoverify(self, ctx, *args: int):
        try:
            if ctx.message.author.id == ctx.message.server.owner.id:
                cursor.execute("SELECT * FROM `auto_verify` WHERE `guild_id`=%s", (ctx.message.server.id,))
                data = cursor.fetchone()
                if data is None:
                    if args.__len__() == 0:
                        embed = discord.Embed(title="Argument Error", description="Please specify what requirements a member needs to meet to be auto-verified", color=0x990000)
                        await self.bot.say(embed=embed)
                    else:
                        cursor.execute("INSERT INTO `auto_verify` (`guild_id`, `enabled`, `avatar_req`, `date_req`, `online_req`) VALUES (%s, 1, %s, %s, %s)", (ctx.message.server.id, args[0], args[1], args[2]))
                        db.commit()
                        embed = discord.Embed(title="Auto-Verify Enabled", description='', color=0x008000)
                        embed.add_field(name='Avatar Required', value=args[0], inline=False)
                        embed.add_field(name='Date Required', value='Epoch:' + str(time.time()) + ' - ' + str(args[1]), inline=False)
                        embed.add_field(name='Online Required', value=args[2], inline=False)
                        await self.bot.say(embed=embed)
                else:
                    if args.__len__() == 0:
                        if data['enabled'] == 0:
                            cursor.execute("UPDATE `auto_verify` SET `enabled`=1 WHERE `guild_id`=%s", (ctx.message.server.id,))
                            embed = discord.Embed(title="Auto-Verify Enabled", description='', color=0x008000)
                            await self.bot.say(embed=embed)
                        if data['enabled'] == 1:
                            cursor.execute("UPDATE `auto_verify` SET `enabled`=0 WHERE `guild_id`=%s", (ctx.message.server.id,))
                            embed = discord.Embed(title="Auto-Verify Disabled", description='', color=0x008000)
                            await self.bot.say(embed=embed)
                    else:
                        if data['enabled'] == 0:
                            cursor.execute("UPDATE `auto_verify` SET `enabled`=1 WHERE `guild_id`=%s", (ctx.message.server.id,))
                            embed = discord.Embed(title="Auto-Verify Enabled", description='', color=0x008000)
                        else:
                            embed = discord.Embed(title="Auto-Verify Requirements Changed", description='', color=0x008000)
                        if args[0] is not None:
                            cursor.execute("UPDATE `auto_verify` SET `avatar_req`=%s WHERE `guild_id`=%s", (args[0], ctx.message.server.id,))
                            embed.add_field(name='Avatar Required', value=args[0], inline=False)
                        if args[1] is not None:
                            cursor.execute("UPDATE `auto_verify` SET `date_req`=%s WHERE `guild_id`=%s", (args[1], ctx.message.server.id,))
                            embed.add_field(name='Date Required', value='Epoch:' + str(time.time()) + ' - ' + str(args[1]), inline=False)
                        if args[2] is not None:
                            cursor.execute("UPDATE `auto_verify` SET `online_req`=%s WHERE `guild_id`=%s", (args[2], ctx.message.server.id,))
                            embed.add_field(name='Online Required', value=args[2], inline=False)
                        db.commit()
                        await self.bot.say(embed=embed)
        except:
            embed = discord.Embed(title="Command Error", description=traceback.format_exc(), color=0x990000)
            await self.bot.say(embed=embed)


def setup(bot):
    bot.add_cog(auto_mod(bot))