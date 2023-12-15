#!/usr/bin/python
#Script de scan port utilizando socket

import socket,sys
from alive_progress import alive_bar

print("\nScript de Port Scan")
ip = input("Digite o IP para realizar o scan de portas: ")
portas = range(1,65535)

with alive_bar(len(portas), title='Consultando portas') as bar:
	for porta in portas:
		meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		meusocket.settimeout(0.5)

		if meusocket.connect_ex((ip,porta)) == 0:
			print("Porta %i"%porta,"aberta")
			meusocket.close()
		bar()
