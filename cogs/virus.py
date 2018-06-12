from lib.virustotal import virt
from cogs import config


class virus():
    def __init__(self, bot):
        self.bot = bot

    virt.apikey = config.read('virust-api-key')