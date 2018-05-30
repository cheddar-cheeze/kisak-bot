import discord
from discord.ext import commands
from utils import config
import sys

class owner():
    def __init__(self, bot):
        self.bot = bot

    __file__ = 'bot.py'

    @commands.command(pass_context=True, no_pm=True)
    async def game(self, ctx, *state):
        await self.bot.send_typing(ctx.message.channel)
        state = ' '.join(state)
        game = discord.Game(name=state)
        if ctx.message.author.id == config.read('owner-id'):
            if state == '':
                await self.bot.change_presence(game=None)
                embed = discord.Embed(title="Game status", description="Kisak's game has been set to ``None``")
                await self.bot.say(embed=embed)
            else:
                await self.bot.change_presence(game=game)
                embed = discord.Embed(title="Game status", description="Kisak's game status has been set to ``" + game.name + "``", color=0xffbc77)
                await self.bot.say(embed=embed)
        else:
            await self.bot.send_typing(ctx.message.channel)
            embed = discord.Embed(title="Command failed", description="This command may only be executed by the bot owner", color=0xffbc77)
            await self.bot.say(embed=embed)

    @commands.command(pass_context=True, no_pm=True)
    async def reload(self, ctx, cog):
        if ctx.message.author.id == config.read('owner-id'):
            await self.bot.send_typing(ctx.message.channel)
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
            embed = discord.Embed(title="Cog-unloaded", description="``" + cog + "`` has been reloaded", color=0xffbc77)
            await self.bot.say(embed=embed)
        else:
            await self.bot.send_typing(ctx.message.channel)
            embed = discord.Embed(title="Command failed", description="This command may only be executed by the bot owner", color=0xffbc77)
            await self.bot.say(embed=embed)

    @commands.command(pass_context=True, no_pm=True)
    async def unload(self, ctx, cog):
        if ctx.message.author.id == config.read('owner-id'):
            await self.bot.send_typing(ctx.message.channel)
            self.bot.unload_extension(cog)
            embed = discord.Embed(title="Cog-unloaded", description="``" + cog + "`` has been unloaded", color=0xffbc77)
            await self.bot.say(embed=embed)
        else:
            await self.bot.send_typing(ctx.message.channel)
            embed = discord.Embed(title="Command failed", description="This command may only be executed by the bot owner", color=0xffbc77)
            await self.bot.say(embed=embed)

    @commands.command(pass_context=True, no_pm=True)
    async def load(self, ctx, cog):
        if ctx.message.author.id == config.read('owner-id'):
            await self.bot.send_typing(ctx.message.channel)
            self.bot.unload_extension(cog)
            embed = discord.Embed(title="Cog-loaded", description="``" + cog + "`` has been loaded", color=0xffbc77)
            await self.bot.say(embed=embed)
        else:
            await self.bot.send_typing(ctx.message.channel)
            embed = discord.Embed(title="Command failed", description="This command may only be executed by the bot owner", color=0xffbc77)
            await self.bot.say(embed=embed)

    @commands.command(pass_context=True, no_pm=True)
    async def restart(self, ctx):
        if ctx.message.author.id == config.read('owner-id'):
            await self.bot.send_typing(ctx.message.channel)
            embed = discord.Embed(title="Restarting...", description="I am restarting!", color=0xffbc77)
            await self.bot.say(embed=embed)
            self.bot.logout()
            await sys.exit(6)
            os.execv(__file__, sys.argv)
        else:
            await self.bot.send_typing(ctx.message.channel)
            embed = discord.Embed(title="Command failed", description="This command may only be executed by the bot owner", color=0xffbc77)
            await self.bot.say(embed=embed)

    @commands.command(pass_context=True, no_pm=True)
    async def shutdown(self, ctx):
        if ctx.message.author.id == config.read('owner-id'):
            await self.bot.send_typing(ctx.message.channel)
            embed = discord.Embed(title="Shutting-down...", description="I am shutting-down!", color=0xffbc77)
            await self.bot.say(embed=embed)
            self.bot.logout()
            await sys.exit(0)
            os.execv(__file__, sys.argv)
        else:
            await self.bot.send_typing(ctx.message.channel)
            embed = discord.Embed(title="Command failed", description="This command may only be executed by the bot owner", color=0xffbc77)
            await self.bot.say(embed=embed)

def setup(bot):
        bot.add_cog(owner(bot))
