import asyncio
import discord
from discord.ext import commands
from utils import config
from utils.constants import embed_color

class mod():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=True)
    async def kick(self, ctx, user: discord.Member=None, *reason):
        if ctx.message.author.server_permissions.ban_members:
            if user is None:
                embed = discord.Embed(title="Error!", description="Please specify a user to kick", color=embed_color)
                await self.bot.say(embed=embed)
            else:
                reason = ' '.join(reason)
                if reason == "":
                    reason = "None was specified"
                g_user: discord.User = user
                await self.bot.send_typing(ctx.message.channel)
                embed = discord.Embed(title=user.name + " was kicked!", description="", color=embed_color)
                embed.add_field(name="User id", value=user.id, inline=True)
                embed.add_field(name="Reason", value=reason, inline=False)
                embed.add_field(name="Server join date", value=user.joined_at, inline=False)
                embed.add_field(name="Discord join date", value=user.created_at.date(), inline=False)
                embed.set_thumbnail(url=user.avatar_url)
                await self.bot.say(embed=embed)
                odm = discord.Embed(title="A member was kicked from your server", description="", color=embed_color)
                odm.add_field(name="Server Name", value=ctx.message.server.name)
                odm.add_field(name="Server id", value=ctx.message.server.id, inline=True)
                odm.add_field(name="User name", value=user.name)
                odm.add_field(name="User id", value=user.id, inline=True)
                odm.add_field(name="Who kicked them", value=ctx.message.author)
                odm.add_field(name="Reason", value=reason, inline=True)
                odm.set_thumbnail(url=user.avatar_url)
                try:
                    await self.bot.send_message(ctx.message.server.owner, embed=odm)
                except:
                    pass
                dm = discord.Embed(title="You were kicked from a server", description="", color=embed_color)
                dm.set_thumbnail(url=ctx.message.server.icon_url)
                dm.add_field(name="Server name", value=ctx.message.server.name)
                dm.add_field(name="Server id", value=ctx.message.server.id, inline=True)
                dm.add_field(name="Reason", value=reason)
                try:
                    await self.bot.send_message(g_user, embed=dm)
                except:
                    pass
                await self.bot.kick(user)
        else:
            embed = discord.Embed(title="Command Error!", description=ctx.message.author.mention + ",you do not have the correct permissions to use this command", color=embed_color)
            await self.bot.say(embed=embed)

    @commands.command(pass_context=True, no_pm=True)
    async def ban(self, ctx, user: discord.Member=None, *reason):
        if ctx.message.author.server_permissions.ban_members:
            if user is None:
                embed = discord.Embed(title="Error!", description="Please specify a user to ban", color=embed_color)
                await self.bot.say(embed=embed)
            else:
                reason = ' '.join(reason)
                if reason == "":
                    reason = "None was specified"
                g_user: discord.User = user
                await self.bot.send_typing(ctx.message.channel)
                embed = discord.Embed(title=user.name + ",was banned!", description="", color=embed_color)
                embed.add_field(name="User id", value=user.id, inline=True)
                embed.add_field(name="Reason", value=reason, inline=False)
                embed.add_field(name="Server join date", value=user.joined_at, inline=False)
                embed.add_field(name="Discord join date", value=user.created_at.date(), inline=False)
                embed.set_thumbnail(url=user.avatar_url)
                await self.bot.say(embed=embed)
                odm = discord.Embed(title="A member was banned from your server", description="", color=embed_color)
                odm.add_field(name="Server Name", value=ctx.message.server.name)
                odm.add_field(name="Server id", value=ctx.message.server.id, inline=True)
                odm.add_field(name="User name", value=user.name)
                odm.add_field(name="User id", value=user.id, inline=True)
                odm.add_field(name="Who banned them", value=ctx.message.author)
                odm.add_field(name="Reason", value=reason, inline=True)
                odm.set_thumbnail(url=user.avatar_url)
                try:
                    await self.bot.send_message(ctx.message.server.owner, embed=odm)
                except:
                    pass
                dm = discord.Embed(title="VAC banned from secure server", description="", color=embed_color)
                dm.add_field(name="Server name", value=ctx.message.server.name)
                dm.add_field(name="Server id", value=ctx.message.server.id, inline=True)
                dm.add_field(name="Reason", value=reason)
                dm.set_thumbnail(url="https://astolfo.life/kisak-assets/vac.png")
                try:
                    await self.bot.send_message(g_user, embed=dm)
                except:
                    pass
                await self.bot.ban(user)
        else:
            embed = discord.Embed(title="Command Error!", description=ctx.message.author.mention + ",you do not have the correct permissions to use this command", color=embed_color)
            await self.bot.say(embed=embed)

    @commands.command(pass_context=True, no_pm=True)
    async def masspm(self, ctx, *message):
        ctx.mesage.delete()
        if ctx.message.author == ctx.message.server.owner:
            message = ' '.join(message)
            if message == "":
                embed = discord.Embed(title="Command Error!", description="You must provide a message to send", color=embed_color)
                await self.bot.say(embed=embed)
            else:
                for user in ctx.message.server.members:
                    try:
                        embed = discord.Embed(title="Mass pm from " + ctx.message.author.name + "#" + ctx.message.author.discriminator, description=message, color=embed_color)
                        embed.set_thumbnail(url=ctx.message.author.avatar_url)
                        await self.bot.send_message(user, embed=embed)
                    except:
                        pass
                embed = discord.Embed(title="Completed masspm!", color=embed_color)
                await self.bot.say(embed=embed)
        else:
            embed = discord.Embed(title="Command Error!", description=ctx.message.author.mention + ",you do not have the correct permissions to use this command", color=embed_color)
            await self.bot.say(embed=embed)

def setup(bot):
    bot.add_cog(mod(bot))
