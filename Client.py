import socket
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
        self.new = deque()
        self.start()

    def run(self):
        self.s.connect((self.SrvrAddr,self.SrvrPort))

        while True:
            ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            newIp = ''
            try:
                newIp = str(self.s.recv(128).decode())
            except:
                pass

            if (len(newIp) > 0):
                #if (str(newIp) != str(self.MyAddr)):
                    if not (newIp in self.group):
                        ss.connect((newIp,self.StrmPort))
                        self.group[newIp] = ss
                        self.new.append(newIp)
                        print("New member: " + str(newIp))

            #time.sleep(2)
        self.s.close ()