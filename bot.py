from util import config
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
        'cogs.misc'
        ]

bot = commands.Bot(command_prefix=config.read('command-prefix'))

@bot.event
async def on_ready():
    print(colored("Kiask-Bot has successfully started up", 'green'))
    config.initialize()
    for cog in cogs:
        bot.load_extension(cog)
        game = discord.Game(name="moderating valve repositories")
        await bot.change_presence(game=game)

@bot.command(pass_context=True, no_pm=True)
@commands.has_role("جبنة الشيدر")
async def reload(ctx, cog=''):
    bot.unload_extension('cogs.' + cog)
    bot.load_extension('cogs.' + cog)
    print(colored(ctx.message.author.name + "#" + ctx.message.author.discriminator + " reloaded a cog", 'yellow'))
    embed = discord.Embed(title="", description="The ``" + cog + "`` cog has been reloaded", color=0xffbc77)
    await bot.say(embed=embed)

@bot.command(pass_context=True, no_pm=True)
@commands.has_role("جبنة الشيدر")
async def unload(ctx, cog=''):
    bot.unload_extension('cogs.' + cog)
    print(colored(ctx.message.author.id + "#" + ctx.message.author.discriminator + " unloaded a cog", 'yellow'))
    embed = discord.Embed(title="Cog-unloaded", description="The ``" + cog + "`` cog has been unloaded", color=0xffbc77)
    await bot.say(embed=embed)

@bot.command(pass_context=True, no_pm=True)
@commands.has_role("جبنة الشيدر")
async def load(ctx, cog=''):
    bot.unload_extension('.cogs' + cog)
    print(colored(ctx.message.author.id + "#" + ctx.message.author.discriminator + " loaded a cog", 'yellow'))
    embed = discord.Embed(title="Cog-loaded", description="The ``" + cog + "`` cog has been loaded", color=0xffbc77)
    await bot.say(embed=embed)

bot.run(token)