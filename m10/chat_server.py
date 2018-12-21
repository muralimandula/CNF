import socket
import threading
from _thread import *
from threading import *
import os
import signal
import time
def check():
	if(active_count() == 2):
		time.sleep(15)
		if(active_count() == 2):
			os.kill(os.getpid(), signal.CTRL_BREAK_EVENT)

def clientthread(conn, addr):
	while True:
		try:
			message = conn.recv(2048)

			for client in client_list:
				if client != conn:
					client.send(message)
		except:
			client_list.remove(conn)
			status = client_dict[conn] + ' is disconnected'
			for client in client_list:
				if(client != conn):
					client.send(status.encode())
			check()
			return 1
	conn.close()

host = '10.10.9.113'
port = 2022
soc = socket.socket()
soc.bind((host, port))
print('Server is ready. Happy Chatting !!')
soc.listen(10)
client_list = []
client_dict = {}
while True:

	conn, addr = soc.accept()
	# conn.send(client_list.encode())
	# print(client_list)
	client_list.append(conn)
	print(str(addr) + ' connected:')
	username = conn.recv(1024).decode()
	client_dict[conn] = username
	Thread(target = clientthread,args = (conn,addr)).start()

	for client in client_list:
		message = str(client_dict[conn])+" is newly added to the group."
		client.send(message.encode())
conn.close()
soc.close()
