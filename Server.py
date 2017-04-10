import socket
import time
from Communication import Communication
from threading import *

class Server(Thread,Communication):
# Maintains many client connections.
    def __init__(self):
        Thread.__init__(self)
        Communication.__init__(self)
        self.clients = []
        self.ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.start()
        print('Server started!',)
        print('Waiting for clients...',)

    def run(self):
        self.ss.bind((self.MyAddr,self.StrmPort))
        for i in range(0,len(self.group)):
            self.ss.listen()
            mbrsock, mbraddr = self.ss.accept()
            mbrIp = str(mbraddr[0])
            if (mbrIp not in self.clients):
                    self.clients.append(mbrsock)
                    print('Broadcast connection est with ' + mbrIp,)
        self._stop