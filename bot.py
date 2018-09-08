from cogs import config
import discord
from discord.ext import commands
from termcolor import colored

token = config.read('token')
cogs = ['cogs.mod',
        'cogs.misc',
        'cogs.logger',
        'cogs.owner',
        'cogs.rep',
        'cogs.account',
        'cogs.verification',
        'cogs.auto_mod'
        ]

bot = commands.Bot(command_prefix=config.read('command-prefix'))

@bot.event
async def on_ready():
    print(colored("Kiask-Bot has successfully started", 'green'))
    config.initialize()
    for cog in cogs:
            bot.load_extension(cog)
    await bot.change_presence(game=discord.Game(name='moderating valve repositories'))

bot.run(token, bot=False)