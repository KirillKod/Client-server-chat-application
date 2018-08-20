from threading import Thread
import socket


class Server:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connections = []

    def __init__(self):
        self.sock.bind((socket.gethostbyname(socket.gethostname()), 8080))
        self.sock.listen(5)

    def handler(self, c, a):
        while 1:
            try:
                data = c.recv(1024)
            except:
                data = None

            if not data:
                self.connections.remove(c)
                c.close()
                disc_output = '{}:{} disconnected'.format(str(a[0]), str(a[1]))
                print(disc_output)
                break
            else:
                for connection in self.connections:
                    connection.send(data)

    def run(self):
        while 1:
            c, a = self.sock.accept()
            con_thread = Thread(target=self.handler, args=(c, a))
            con_thread.daemon = True
            con_thread.start()
            self.connections.append(c)
            con_output = '{}:{} connected'.format(str(a[0]), str(a[1]))
            print (self.connections)
            print(con_output)


Server().run()
