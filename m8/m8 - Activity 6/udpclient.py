import socket
def main():
	host = '10.10.9.113'
	port = 4502
	server = ('10.10.9.113', 4563)

	soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	soc.bind((host, port))
	message = input("Client Input : ")
	while message != '.':
		soc.sendto(message.encode(), server)
		data, addr = soc.recvfrom(1024)
		print('Received from server as : ' + str(data.decode()))
		message = input("Client Input : ")
	soc.close()

if __name__ == '__main__':
	main()
