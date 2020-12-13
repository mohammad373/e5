# e5


import os
import sys
import socket
import time
import requests
from colorama import Fore

def __target__():
    os.system("clear")
    time.sleep(1)
    print(Fore.YELLOW + "Hello , Welcome ;)\n")
    time.sleep(1)
    print(Fore.RED + "This Is Text Me By DDOS ;)")
    time.sleep(0.5)
    target = input(Fore.BLUE + "\n[" + Fore.RED + "!" + Fore.BLUE + "]" + Fore.RED + " ~ " + Fore.GREEN + "Pleass Enter Your Address Target" + Fore.YELLOW + " ==>  ")
    if target == "" or None :
        try:
            time.sleep(0.4)
            print(Fore.RED + "\n[!] ~ Error Your Target Is Not Found Or None ;(")
            time.sleep(1)
            sys.exit()
        except:
            pass
    s = socket.gethostbyname(target)
    r = requests.get(s)
    if r.status_code == 200:
        print("Yesss")
    else:
        print("NOOOOO")
__target__()
