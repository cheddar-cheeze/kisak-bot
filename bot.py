from cogs import config, database
import discord
from discord.ext import commands
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
        'cogs.logger',
        'cogs.owner',
        'cogs.rep'
        ]

bot = commands.Bot(command_prefix=config.read('command-prefix'))

@bot.event
async def on_ready():
    print(colored("Kiask-Bot has successfully started", 'green'))
    config.initialize()
    for cog in cogs:
            bot.load_extension(cog)
    await bot.change_presence(game=discord.Game(name='moderating valve repositories'))
    database.initialize()

bot.run(token)