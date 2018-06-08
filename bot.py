from utils import config
import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot
from termcolor import colored
import os
import platform
import sys
from utils import database

if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')

token = config.read('token')
cogs = ['cogs.mod',
        'cogs.misc',
        'utils.logger',
        'cogs.owner',
        'cogs.rep'
        ]

bot = commands.Bot(command_prefix=config.read('command-prefix'))

@bot.event
async def on_ready():
    print(colored("Kiask-Bot has successfully started", 'green'))
    config.initialize()
    for cog in cogs:
        try:
            bot.load_extension(cog)
        except:
            pass
    await bot.change_presence(game=discord.Game(name='moderating valve repositories'))
    database.initialize()


bot.run(token)