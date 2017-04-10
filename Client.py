import socket
import select
from threading import *
from collections import deque
import time
from Play import Play
from Communication import Communication

class Client(Thread,Communication):
# Maintains one server connection and group info.
    def __init__(self):
        Thread.__init__(self)
        Communication.__init__(self)
        #self.daemon = True
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.group = {}
        self.groupsocks = []
        self.srvrsock = []
        self.start()

    def run(self):
        self.s.connect((self.SrvrAddr,self.SrvrPort))
        self.srvrsock.append(s)

        while True:
            ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            newIp = ''
            self.srvrsockready,_,_ = select.select(self.srvrsock, [], []) 
            self.groupsocksready,_,_ = select.select(self.groupsocks, [], []) 
            for sock in srvrsockready:
                try:
                    newIp = str(sock.recv(128).decode())
                except:
                    pass

            if (len(newIp) > 0):
                if not (newIp in self.group):
                    if (str(newIp) != str(self.MyAddr)):
                        ss.connect((newIp,self.StrmPort))
                        self.group[newIp] = ss
                        self.groupsocks.append(ss)
                        print("New member: " + str(newIp))

            #time.sleep(2)
        self.s.close ()