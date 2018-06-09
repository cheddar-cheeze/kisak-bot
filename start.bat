@echo off
color 06
echo "Checking github for updates"
color 09
git pull
color 02
echo "Git repository is up to date"
timeout /t 1
color 09
pip install --upgrade -r requirements.txt
color 02
echo "Python packages are up to date"
timeout /t 1
color 05
echo "Kiask-Bot is starting up"
timeout /t 2
cls
run bot.py