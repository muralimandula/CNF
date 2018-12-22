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

print('\n--------ATTENDANCE MARKING - TCP Communication-----------\n')
roll_list = [20158501, 20158502, 20158503, 20158504, 20158505,
 				20158506, 20158507, 20158508, 20158509, 20158510]
string  = str(roll_list[0])
print('Students in the class:')
for i in range(1, len(roll_list)):
	string = string + ' - ' +str(roll_list[i])
print(string)

host = '10.10.9.113'
port = 2022
soc = socket.socket()
soc.bind((host, port))
soc.listen(10)
client_list = []
quest_anslist = ["What is my first vehicle first number?501",
	"What is my masters degree?MSIT",
	"Who is my close friend?Sriram",
	"When did you meet your close friend?1999",
	"Whatâ€™s your mother's maiden name?John",
	"Who invented telephone?Graham Bell",
	"Who invented radium?Madam Curie",
	"Which country is called as land of rising sun?Japan",
	"Which country is called of white elephants?Thailand",
	"Gateway of India?Mumbai"]
client_dict = {}
while True:

	conn, addr = soc.accept()
	client_list.append(conn)
	print(str(addr) + ' connected:')
	rollnum = conn.recv(1024).decode()

	# print(rollnum, roll_list[0])
	checkroll = int(rollnum)

	if checkroll in roll_list:
		quest_index = roll_list.index(checkroll)
		question = 'SECRETQUESTION - ' + quest_anslist[quest_index].split("?")[0] + '?'
		answer = quest_anslist[quest_index].split("?")[1]

		conn.send(question.encode())

		reply = conn.recv(1024).decode()
		if reply == answer:
			conn.send('ATTENDANCE-SUCCESS'.encode())



		client_dict[conn] = rollnum


	else:
		conn.send('ROLLNUM-NOTFOUND'.encode())
	# client_dict[conn] = rollnum
	Thread(target = clientthread,args = (conn,addr)).start()

	# for client in client_list:
	# 	message = str(client_dict[conn])+" is newly added to the group."
	# 	client.send(message.encode())
conn.close()
soc.close()
