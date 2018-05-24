import json
import os
from termcolor import colored
import colorama
import platform

if platform.system() == 'Windows':
    directory = '\\'
else:
    directory = '/'

config_path = os.getcwd()

def initialize():
    json.load(open(config_path + directory + 'config.json'))
    print(colored("Config has successfully loaded from: "+config_path + directory + "config.json", 'green'))


def read(data):
    output = json.load(open(config_path + directory + 'config.json'))[data]
    return output