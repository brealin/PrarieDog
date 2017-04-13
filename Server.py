from Communication import Communication
from threading import *
import socket

class Server(Thread,Communication):
# Maintains many client connections.
    def __init__(self):
        Thread.__init__(self)
        Communication.__init__(self)
        self.clients = []
        self.ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.start()
        print('Broadcasting, waiting for member(s) to connect...',)

    def run(self):
        self.ss.bind((self.MyAddr,self.SrvrPort))
        for i in range(0,len(self.group)):
            self.ss.listen()
            mbrsock, mbraddr = self.ss.accept()
            mbrIp = str(mbraddr[0])
            if (mbrIp not in self.clients):
                    self.clients.append(mbrsock)
                    print('Broadcast connection est with ' + mbrIp + '  ',)
        self._stop