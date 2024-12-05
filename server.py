import socket
from threading import Thread

IP_ADDR = '127.0.0.1'
PORT = 5550
SERVER = None
BUFFER_SIZE = 4096

clients={}

def accept_connection():
    global SERVER
    global clients

    while True:
        client,addr = SERVER.accept()
        print(client,addr)

def setup():
    global IP_ADDR
    global PORT
    global SERVER

    SERVER=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.bind((IP_ADDR,PORT))
    SERVER.listen(100)

    print("\t\t\t\tSERVER IS WAITING FOR INCOMMING CONNECTIONS...\n")

    accept_connection()

setup_thread = Thread(target=setup)
setup_thread.start()