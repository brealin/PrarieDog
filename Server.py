import socket
import time
from Communication import Communication
from threading import *

class Server(Thread,Communication):
# Maintains many client connections.
    def __init__(self):
        Thread.__init__(self)
        Communication.__init__(self)
        self.clients = {}
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
        self.start()
        print('Server started!',)
        print('Waiting for clients...',)

    def run(self):        
        self.s.bind((self.SrvrAddr,self.SrvrPort))

        while True:
            newIp = ''
            newAddr = ('','')
            newsock = None
            self.s.listen()                                # Now wait for client connection.
            newsock, newAddr = self.s.accept()             # Establish connection with client.
            newIp = str(newAddr[0])
            print('Got connection from ' + newIp,)

            if (newIp not in self.clients):
                self.clients[newIp] = newsock

            for k in self.clients:                          #Send the new client every client and every client the new client                 #key=ip, value=sock
                for key, value in self.clients.items():
                    value.send(k.encode())
                    time.sleep(2)

        self.s.close()