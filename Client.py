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
        self.groupsocks = []
        self.groupsocksready = []
        self.start()

    def run(self):
        for ip in self.group:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,self.StrmPort))
            self.groupsocks.append(s)
            print("New member: " + str(ip))

        while True:
            try:
                self.groupsocksready,_,_ = select.select(self.groupsocks, [], [])
            except:
                pass 