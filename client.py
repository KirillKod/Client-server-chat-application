from threading import Thread
import socket
import sys


class Client:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #in case if it's remote machine, then argument with server address needs to be passed
    server_address = socket.gethostbyname(socket.gethostname()) if len(sys.argv) == 1 else sys.argv[1]

    def __init__(self, address=server_address):
        self.sock.connect((address, 8080))
        print('Enter your name:')
        self.name = input('')

        input_thread = Thread(target=self.send_message)
        input_thread.daemon = True
        input_thread.start()

        while 1:
            data = self.sock.recv(1024)
            if not data:
                break
            print(data)

    def send_message(self):
        while 1:
            message = self.name + ":" + input('')
            self.sock.send(bytes(message, 'utf-8'))


Client()


