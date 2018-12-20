import socket
def main():
	dollar = {'INR': 67.0, 'yern': 113.41, 'pounds': 0.75}
	INR = {'dollar': 0.014, 'yern': 1.58 , 'pounds': 0.11}
	pounds = {'dollar': 1.26, 'yern': 142 , 'INR': 90.0}
	yern = {'dollar': 0.0089 , 'INR': 0.63 , 'pounds': 0.007}
	lst = [dollar, INR, pounds, yern]
	host  = '10.2.136.120'
	port = 2012

	soc = socket.socket()
	soc.bind((host, port))
	soc.listen(1)
	client, address = soc.accept()
	print('connection from ' + str(address))
	while True:
		data = client.recv(1024)
		data = str(data.decode()).split()

		if data[1] == 'dollar':
			result = float(dollar.get(data[4]) * int(data[2]))

		elif data[1] == 'INR':
			result = float(INR.get(data[4]) * int(data[2]))

		elif data[1] == 'yern':
			result = float(yern.get(data[4]) * int(data[2]))

		elif data[1] == 'pounds':
			result = float(pounds.get(data[4]) * int(data[2]))
		print('sending:' + str(result))
		client.send(str(result).encode())
	client.close()


if __name__ == '__main__':
	main()
