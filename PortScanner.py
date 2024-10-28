import os
import socket
import threading
os.system('cls' if os.name == 'nt' else 'clear')

def logo():
        print("""\033[1;94m


     ╔═══════════════════════╗
     ║   PortScanner Tool    ║
     ║   by Vinicius Viana   ║
     ╚═══════════════════════╝
        
\033[1;m""")
logo()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input("Informe o IP que deseja realizar o scan: ")
port = int(input("Informe a porta que deseja realizar o scan: "))

def PortScanner(port):
    if s.connect_ex((host, port)):
        print(f"A porta {port} está fechada")
    else:
        print(f"A porta {port} está aberta")

PortScanner(port)