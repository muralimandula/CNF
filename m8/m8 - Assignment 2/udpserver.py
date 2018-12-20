import socket
def main():
	dollar = {'INR': 67.0, 'yern': 113.41, 'pounds': 0.75}
	INR = {'dollar': 0.014, 'yern': 1.58 , 'pounds': 0.11}
	pounds = {'dollar': 1.26, 'yern': 142 , 'INR': 90.0}
	yern = {'dollar': 0.0089 , 'INR': 0.63 , 'pounds': 0.007}
	lst = [dollar, INR, pounds, yern]
	host = '10.2.136.120'
	port = 5095

	soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	soc.bind((host, port))
	while True:
		data, address = soc.recvfrom(1024)
		print('message from: ' + str(address))
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
		soc.sendto(str(result).encode(), address)
	soc.close()

if __name__ == '__main__':
	main()
