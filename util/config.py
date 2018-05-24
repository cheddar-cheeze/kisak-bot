import json
import os
from termcolor import colored
import colorama

config_path = os.getcwd()

def initialize():
    json.load(open(config_path+'/config.json'))
    print(colored("Config has successfully loaded from: "+config_path+"/config.json", 'green'))


def read(data):
    output = json.load(open(config_path+'/config.json'))[data]
    return output