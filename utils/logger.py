import discord
from discord.ext import commands
import os
import platform
import logging
from utils import config

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
        if message.author.id == '316627148221972491':
            try:
                await self.bot.send_message(message.channel, "Marc is a weeb")
            except:
                pass
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        if not os.path.exists(log_path + directory + message.server.name):
            os.makedirs(log_path + message.server.name)
        channel_path = log_path + message.server.name
        if not os.path.exists(channel_path):
            os.makedirs(channel_path)
        try:
            channel = channel_path + directory + message.channel.name
            log = open(channel + ".txt", "a+")
            log.write(str(message.timestamp) + "  " + str(message.author) + ":" + message.content + '\n')
            log.close()
        except:
            pass

def setup(bot):
    bot.add_cog(logger(bot))