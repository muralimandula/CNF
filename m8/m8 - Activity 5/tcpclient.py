import socket
def Main():
	host = '10.10.9.113'
	port = 2012

	soc = socket.socket()
	soc.connect((host, port))
	message = input("Client Input : ")
	while message != '.':
		soc.send(message.encode())
		data = soc.recv(1024)
		print('Received from server as : ' + str(data.decode()))
		message = input("Client Input : ")
	soc.close()


if __name__ == '__main__':
	Main()
