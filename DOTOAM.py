import os
import sys
import time
import socket

lor_off="\033[0m"       # Text Reset
black="\033[0;30m"        # Black
red="\033[0;31m"          # Red
green="\033[0;32m"        # Green
yellow="\033[0;33m"       # Yellow
blue="\033[0;34m"         # Blue
purple="\033[0;35m"       # Purple
cyan="\033[0;36m"         # Cyan
white="\033[0;37m"        # White


os.system("clear")
logo=(red+"""

 __          ___    _ _____ _______ ______ 
 \ \        / / |  | |_   _|__   __|  ____|
  \ \  /\  / /| |__| | | |    | |  | |__   
   \ \/  \/ / |  __  | | |    | |  |  __|  
    \  /\  /  | |  | |_| |_   | |  | |____ 
     \/  \/   |_|  |_|_____|  |_|  |______|
                                           
                                           
""")
logo2=(green+"""

______ _____    _____ _     
|  _  \  ___|  |_   _| |    
| | | | |____   _| | | |    
| | | |  __\ \ / / | | |    
| |/ /| |___\ V /| |_| |____
|___/ \____/ \_/\___/\_____/
                            
                            
""")
print(logo+logo2)
print(purple+"                     LOGIN PANAL ©©©©©")

def Writertext(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.07)




usern="WDDTI"
passwd="WDDTI"


inpuser=str(input("\n\n         TOOL USERNAME>>> "))
inppass=str(input("\n\n         TOOL PASSWORD>>> "))

if usern==inpuser and passwd== inppass:
	os.system("clear")
	Writertext(yellow+"        {√} username & password correct [√]")
	os.system("clear")
	Writertext(green+"      LOGIN Successful.........")
	pass
else:
	os.system("clear")
	Writertext(red+"username and password wrong [x]")
	
	sys.exit()
	
	
os.system("clear")

wd=(green+""".=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-.
|                     ______                     |
|                  .-"      "-.                  |
|                 /            \                 |
|     _          |              |          _     |
|    ( \         |,  .-.  .-.  ,|         / )    |
|     > "=._     | )(__/  \__)( |     _.=" <     |
|    (_/"=._"=._ |/     /\     \| _.="_.="\_)    |
|           "=._"(_     ^^     _)"_.="           |
|               "=\__|IIIIII|__/="               |
|              _.="| \IIIIII/ |"=._              |
|    _     _.="_.="\          /"=._"=._     _    |
|   ( \_.="_.="     `--------`     "=._"=._/ )   |
|    > _.="                            "=._ <    |
|   (_/\033[0;35m WHITE_DEVIL  \033[0;32m                      \_)   |
|                                                |
'-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-='""")
print(wd)

def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./10)
slowprint(cyan+"                 WELCOME TO WHITE DEVIL TOOL")
print(yellow+"\n\n===========================================================================================================================================")
url = str(input(yellow+"\n\n\nEnter your target web url :"))

def getip(url):
	ip=socket.gethostbyname(url)
	return ip
	
ip=getip(url)
print(ip)


