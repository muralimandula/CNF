import socket
def main():
	host = '10.10.9.113'
	port = 2012
	soc = socket.socket()
	soc.bind((host, port))
	soc.listen(1)


	client, address = soc.accept()
	print('Server Info : ' + str(address))
	while True:
		data = client.recv(1024)
		if not data:
			break
		giventext = str(data.decode())
		print('Text from client : ' + giventext)
		data = giventext.upper()
		print('Sending : ' + str(data))
		client.send(data.encode())
	client.close()

if __name__ == '__main__':
	main()

