import socket
import threading
import random
from _thread import *
def clientthread(conn, address):
    welcome_note = 'welcome to Guess my Number! \n I am thinking of a number number between 1 and 50. Try to guess it in as few attempts as possible.'
    hi = 'Your guess is greater than the value!'
    lo = 'Your guess is lesser than the value!'
    guessesCount = 0
    conn.send(welcome_note.encode())
    x = random.randint(1, 51)
    data = conn.recv(1024)
    print('User Info' + ' : ' +str(address) + ' '+ str(data.decode()))
    conn.send(''.encode())
    while True:
        answer = conn.recv(1024)

        print('Guess :  ' + answer.decode())
        if (int(answer.decode()) > x):
            conn.send(hi.encode())
            guessesCount += 1
        elif (int(answer.decode()) < x):
            conn.send(lo.encode())
            guessesCount += 1
        else:
            guessesCount += 1
            correct = 'Correct, number of guesses is '+ str(guessesCount)
            conn.send(correct.encode())
            break

    conn.close()
    print('Connection is closed.')

host = '10.2.136.120'
port  = 2025
soc = socket.socket()
soc.bind((host, port))
soc.listen(5)
print('socket is ready')
while True:
    connection, address = soc.accept()
    print('connected from  ' + str(address))
    start_new_thread(clientthread, (connection, address))
soc.close()

