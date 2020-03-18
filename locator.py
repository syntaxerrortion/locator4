import os

os.system("pkg install figlet -y")
os.system("pkg install php -y")
os.system("pkg install git -y")
os.system("pkg install wget -y")
os.system("clear")

os.system("git clone https://github.com/thelinuxchoice/locator.git")
os.system("cd locator/ && bash locator.sh")
