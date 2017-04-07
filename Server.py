import socket
import time
from Communication import Communication
from threading import *

class Server(Thread,Communication):
# Maintains many client connections.
    def __init__(self, host):
        Thread.__init__(self)
        Communication.__init__(self)
        self.host = host
        self.clients = {}
        self.members = {}
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.start()
        print('Server started!',)
        print('Waiting for clients...',)

    def run(self):
        self.ss.bind((self.MyAddr,self.StrmPort))
        if self.host:
            self.s.bind((self.MyAddr,self.SrvrPort))

        while True:
            skip = False        
            if self.host:
                newIp = ''
                newAddr = ('','')
                newsock = None
                self.s.listen()                                # Now wait for client connection.
                newsock, newAddr = self.s.accept()             # Establish connection with client.
                newIp = str(newAddr[0])
               
                if (newIp not in self.clients):
                    #if (str(newIp) != str(self.MyAddr)):
                    self.clients[newIp] = newsock
                    print('Got connection from ' + newIp,)
                    if (str(newIp) == str(self.MyAddr)):
                        skip = True

                for k in self.clients:                          #Send the new client every client and every client the new client                 #key=ip, value=sock
                    for key, value in self.clients.items():
                        value.send(k.encode())
            if not skip:
                self.ss.listen()
                mbrsock, mbraddr = self.ss.accept()
                mbrIp = str(mbraddr[0])
                if (mbrIp not in self.members):
                    if (str(mbrIp) != str(self.MyAddr)):
                        self.members[mbrIp] = mbrsock
                        print('Broadcast connection est with ' + mbrIp,)

            #time.sleep(2)
        self.s.close()