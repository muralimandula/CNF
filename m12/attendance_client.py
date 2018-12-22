import socket
import threading

def receive(s, rollnum):
    while True:

        try:
            data = s.recv(1024).decode()
            if not data:
                continue
            print (str(data))

        except:
            print("Sucessfully Disconnected.")
            break


def main():
    host = '10.10.9.113'
    port = 2022

    soc = socket.socket()
    soc.connect((host, port))


    print('\n-------MSIT Attendance marking - 2015-------\n')
    print('Enter your rollnumber : ', end = " ")
    rollnum = input()
    print('\n')
    soc.send(rollnum.encode())
    flag = 0

    threading.Thread(target = receive, args = (soc, rollnum)).start()
    message = ''
    while message != '.' and flag != 1:

        sending = input('SECRETANSWER - ')
        soc.send(sending.encode())
        flag = 1


    soc.close()

if __name__ == "__main__":
    main()
