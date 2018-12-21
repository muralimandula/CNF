import socket
import threading

def receive(s, username):
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
    # print(soc.recv(1024).decode())
    print('-------Welcome to private group Chat--------')


    # print(soc.recv(1024).decode())
    print('Enter your name : ', end = " ")
    username = input()
    print('\n')
    soc.send(username.encode())
    threading.Thread(target = receive, args = (soc, username)).start()
    message = ''
    while message != '.':
        # print('Me : ', end = " ")
        message = input()
        sending = '         ' + username + ': ' + message
        soc.send(sending.encode())

    soc.close()

if __name__ == "__main__":
    main()
