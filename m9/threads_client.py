import socket
def main():
	host = '10.2.136.120'
	port  = 2025

	soc = socket.socket()
	soc.connect((host, port))
	message = input('Username : ')
	while message != '.':
		soc.send(message.encode())
		data = soc.recv(1024)
		print(' ---- ' + str(data.decode()))
		if str(data.decode()).split(' ')[0] == 'Correct,':
			break
		message = input('Enter your guess: ')

	soc.close()

if __name__ == '__main__':
	main()
