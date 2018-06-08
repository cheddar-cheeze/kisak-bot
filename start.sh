#!/bin/bash
txtrst=$(tput sgr0)
txtyellow=$(tput setaf 3)
txtgreen=$(tput setaf 2)
txtcyan=$(tput setaf 6)
txtpurple=$(tput setaf 5)
echo "${txtyellow}Checking github for updates${txtcyan}"
git pull http master
echo "${txtgreen}Git repository is up to date"
sleep 1
echo "${txtyellow}Checking pip for updates${txtcyan}"
python3.6 -m pip install -r requirements.txt
echo "${txtgreen}Python packages are up to date"
sleep 1
echo "${txtpurple}Kiask-Bot is starting up${txtrst}"
sleep 2
clear
python3.6 bot.py