import discord
from discord.ext import commands
import os
import platform

if platform.system() == 'Windows':
    directory = '\\'
else:
    directory = '/'

path = os.getcwd()
log_path = path + directory + 'channel_logs' + directory

class logger():
    def __init__(self, bot):
        self.bot = bot


    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        if not os.path.exists(log_path + message.server.name):
            os.makedirs(log_path + message.server.name)
        channel_path = log_path + message.server.name + directory + message.channel.name
        log = open(channel_path + ".txt", "a+")
        log.write(str(message.timestamp) + "|Message author:" + str(message.author) + "|" + message.content + '\n')
        log.close()

def setup(bot):
    bot.add_cog(logger(bot))
