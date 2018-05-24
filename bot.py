from utils import config
import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot
from termcolor import colored
import os
import platform

if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')

token = config.read('token')
cogs = ['cogs.mod',
        'cogs.misc',
        'utils.logger'
        ]

bot = commands.Bot(command_prefix=config.read('command-prefix'))

@bot.event
async def on_ready():
    print(colored("Kiask-Bot has successfully started", 'green'))
    config.initialize()
    for cog in cogs:
        bot.load_extension(cog)
    game = discord.Game(name="moderating valve repositories")
    await bot.change_presence(game=game)


@bot.command(pass_context=True, no_pm=True)
async def unload(ctx, cog=''):
    if ctx.message.author.id == config.read('owner-id'):
        await bot.send_typing(ctx.message.channel)
        bot.unload_extension(cog)
        embed = discord.Embed(title="Cog-unloaded", description="``" + cog + "`` has been unloaded", color=0xffbc77)
        await bot.say(embed=embed)
    else:
        await bot.send_typing(ctx.message.channel)
        embed = discord.Embed(title="Command failed", description="This command may only be executed by the bot owner", color=0xffbc77)
        await bot.say(embed=embed)


@bot.command(pass_context=True, no_pm=True)
async def load(ctx, cog=''):
    if ctx.message.author.id == config.read('owner-id'):
        await bot.send_typing(ctx.message.channel)
        bot.unload_extension(cog)
        embed = discord.Embed(title="Cog-loaded", description="``" + cog + "`` has been loaded", color=0xffbc77)
        await bot.say(embed=embed)
    else:
        await bot.send_typing(ctx.message.channel)
        embed = discord.Embed(title="Command failed", description="This command may only be executed by the bot owner", color=0xffbc77)
        await bot.say(embed=embed)


bot.run(token)