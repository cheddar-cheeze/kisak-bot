import discord
from discord.ext import commands
import os
import traceback
from cogs.constants import embed_color
from cogs.database import Session

class misc():
    def __init__(self, bot):
        self.bot = bot

    async def on_server_join(self, server):
        db = Session().db
        cursor = db.cursor()
        cursor.execute("SELECT * FROM `welcome_message` WHERE `guild_id`=%s", (server.id,))
        wel = cursor.fetchone()
        if wel is None:
            cursor.execute("INSERT INTO `welcome_message` (`guild_id`, `channel_id`, `enabled`, `message`) VALUES (%s, NULL, 0, NULL)", (server.id,))
            db.commit()
        cursor.execute()
        lev = cursor.fetchone("SELECT * FROM `leave_message` WHERE `guild_id`=%s", (server.id,))
        if lev is None:
            cursor.execute("INSERT INTO `leave_message` (`guild_id`, `channel_id`, `enabled`, `message`) VALUES (%s, NULL, 0, NULL)", (server.id,))
            db.commit()
        db.close()

    async def on_member_join(self, member):
        db = Session().db
        cursor = db.cursor()
        cursor.execute("SELECT `message`, `channel_id` FROM `welcome_message` WHERE `guild_id`=%s AND `enabled`=1", (member.server.id,))
        data = cursor.fetchone()
        if data is not None:
            message = data['message'].replace('%m', member.mention)
            embed = discord.Embed(title="Member joined!", description=message, color=embed_color)
            embed.set_thumbnail(url=member.avatar_url)
            await self.bot.send_message(discord.Object(id=data['channel_id']), embed=embed)
        db.close()

    async def on_member_remove(self, member):
        db = Session().db
        cursor = db.cursor()
        cursor.execute("SELECT `message`, `channel_id` FROM `leave_message` WHERE `guild_id`=%s AND `enabled`=1", (member.server.id,))
        data = cursor.fetchone()
        if data is not None:
            message = data['message'].replace('%m', member.mention)
            embed = discord.Embed(title="Member Left!", description=message, color=embed_color)
            embed.set_thumbnail(url=member.avatar_url)
            await self.bot.send_message(discord.Object(id=data['channel_id']), embed=embed)
        db.close()

    @commands.command(pass_context=True, no_pm=True)
    async def welcome(self, ctx, channel:discord.Channel=None, *message):
        db = Session().db
        cursor = db.cursor()
        if ctx.message.author == ctx.message.server.owner.id:
            try:
                if channel is None:
                    channel = ctx.message.channel
                if message == '':
                    message = 'Welcome to-' +ctx.message.server.name + '-%m'
                else:
                    message = ' '.join(message)
                cursor.execute("SELECT * FROM `welcome_message` WHERE `guild_id`=%s", (ctx.message.server.id,))
                check = cursor.fetchone()['enabled']
                if check == 0:
                    cursor.execute("UPDATE `welcome_message` SET `channel_id`=%s, `enabled`=1, `message`=%s WHERE `guild_id`=%s", (channel.id, message, ctx.message.server.id,))
                    db.commit()
                    embed = discord.Embed(title='Welcome Message Enabled', description='', color=0x008000)
                    embed.add_field(name='Channel', value=channel.mention)
                    embed.add_field(name='Message', value=str(message), inline=True)
                    await self.bot.say(embed=embed)
                else:
                    cursor.execute("UPDATE `welcome_message` SET `enabled`=0 WHERE `guild_id`=%s", (ctx.message.server.id,))
                    db.commit()
                    embed = discord.Embed(title='Welcome Message Disabled', description='', color=0x008000)
                    embed.add_field(name='Channel', value=channel.mention)
                    await self.bot.say(embed=embed)
            except:
                embed = discord.Embed(title="An Error Occurred!", description=traceback.format_exc(), color=0x990000)
                await self.bot.say(embed=embed)
            db.close()


    @commands.command(pass_context=True, no_pm=True)
    async def leave(self, ctx, channel: discord.Channel=None, *message):
        db = Session().db
        cursor = db.cursor()
        if ctx.message.author.id == ctx.message.server.owner.id:
            try:
                if channel is None:
                    channel = ctx.message.channel
                if message == '':
                    message = 'Welcome to-' + ctx.message.server.name + '-%m'
                else:
                    message = ' '.join(message)
                cursor.execute("SELECT * FROM `leave_message` WHERE `guild_id`=%s", (ctx.message.server.id,))
                check = cursor.fetchone()['enabled']
                if check == 0:
                    cursor.execute("UPDATE `leave_message` SET `channel_id`=%s, `enabled`=1, `message`=%s WHERE `guild_id`=%s", (channel.id, message, ctx.message.server.id,))
                    db.commit()
                    embed = discord.Embed(title='Leave Message Enabled', description='', color=0x008000)
                    embed.add_field(name='Channel', value=channel.mention)
                    embed.add_field(name='Message', value=str(message), inline=True)
                    await self.bot.say(embed=embed)
                else:
                    cursor.execute("UPDATE `leave_message` SET `enabled`=0 WHERE `guild_id`=%s", (ctx.message.server.id,))
                    db.commit()
                    embed = discord.Embed(title='Leave Message Disabled', description='', color=0x008000)
                    embed.add_field(name='Channel', value=channel.mention)
                    await self.bot.say(embed=embed)
            except:
                embed = discord.Embed(title="An Error Occurred!", description=traceback.format_exc(), color=0x990000)
                await self.bot.say(embed=embed)
            db.close()

    @commands.command(pass_context=True, no_pm=True)
    async def info(self, ctx, user: discord.Member=None):
        db = Session().db
        cursor = db.cursor()
        if user is None:
            user = ctx.message.author
        cursor.execute("SELECT `value` FROM `rep` WHERE `guild_id`=%s AND `user_id`=%s", (ctx.message.server.id, user.id,))
        data = cursor.fetchone()
        if data is None:
            cursor.execute("INSERT INTO `rep` (`guild_id`, `user_id`, `value`) VALUES (%s, %s, 0)", (ctx.message.server.id, user.id,))
            db.commit()
            rep = str(0)
        else:
            rep = str(data['value'])
        if user is None:
            await self.bot.send_typing(ctx.message.channel)
            embed = discord.Embed(title=ctx.message.author.name + "'s info", description="", color=embed_color)
            embed.set_thumbnail(url=ctx.message.author.avatar_url)
            embed.add_field(name="User id", value=ctx.message.author.id)
            embed.add_field(name="Rep", value=rep, inline=True)
            embed.add_field(name="Server join date", value=ctx.message.author.joined_at)
            embed.add_field(name="Discord join date", value=ctx.message.author.created_at.date(), inline=True)
            embed.add_field(name="Status", value=ctx.message.author.status)
            await self.bot.say(embed=embed)
        else:
            await self.bot.send_typing(ctx.message.channel)
            embed = discord.Embed(title=user.name + "'s info", description="", color=embed_color)
            embed.set_thumbnail(url=user.avatar_url)
            embed.add_field(name="User id", value=user.id)
            embed.add_field(name="Rep", value=rep, inline=True)
            embed.add_field(name="Server join date", value=user.joined_at)
            embed.add_field(name="Discord join date", value=user.created_at.date(), inline=True)
            embed.add_field(name="Status", value=user.status)
            await self.bot.say(embed=embed)
        db.close()

    @commands.command(pass_context=True, no_pm=True)
    async def server(self, ctx):
        await self.bot.send_typing(ctx.message.channel)
        embed = discord.Embed(title="Server info", description="", color=embed_color)
        embed.set_thumbnail(url=ctx.message.server.icon_url)
        embed.add_field(name="Server name", value=ctx.message.server.name)
        embed.add_field(name="Server id", value=ctx.message.server.id, inline=True)
        embed.add_field(name="Owner", value=ctx.message.server.owner.name)
        embed.add_field(name="Server region", value=ctx.message.server.region, inline=True)
        embed.add_field(name="Member count", value=ctx.message.server.member_count)
        embed.add_field(name="Server creation date", value=ctx.message.server.created_at, inline=True)
        embed.add_field(name="Verification level", value=ctx.message.server.verification_level)
        await self.bot.say(embed=embed)


    @commands.command(pass_context=True, no_pm=True)
    async def unacceptable(self, ctx):
        await self.bot.delete_message(ctx.message)
        await self.bot.send_file(destination=ctx.message.channel, fp='assets/unacceptable.png')

def setup(bot):
    bot.add_cog(misc(bot))