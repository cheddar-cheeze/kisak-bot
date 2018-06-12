import platform
import sqlite3
import os

if platform.system() == 'Windows':
    directory = '\\'
else:
    directory = '/'

path = os.getcwd()
db_path = path + directory + "bot.db"
connection = sqlite3.connect(db_path)

cursor = connection.cursor()


def initialize():
    cursor.execute("""CREATE TABLE IF NOT EXISTS 'rep' ('user_id' INT PRIMARY KEY ,'rep_val' INT);""")
    cursor.execute("CREATE TABLE IF NOT EXISTS 'warnings' ('server_id' INT PRIMARY KEY, 'user_id' INT, 'reason' TEXT);""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS 'xp' ('user_id' INT PRIMARY KEY, 'level' INT, 'xp_amt' INT);""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS  'mspam'('sever_id' INT PRIMARY KEY , 'amt' int, 'punishment' INT, 'state' BIT);""")
    connection.commit()