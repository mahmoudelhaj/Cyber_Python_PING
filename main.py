import subprocess
from termcolor import colored
from art import *

tprint("ping",font="block",chr_ignore=True)
print("----------CyberPython----------")
print("")

host = input("What is your IP? \n")
result = subprocess.call(['ping',host],stdout=subprocess.PIPE)

if result == 0 :
    print(colored('The Host is UP','green'))
else:
    print(colored('The Host is DOWN','red'))