from threading import *
from Communication import Communication
import select
import socket

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
            s.settimeout(30)
            c = False
            while not c:
                try:
                    s.connect((ip,self.StrmPort))
                    c = True
                except socket.error as exc:
                    print("Caught exception socket.error : %s" % exc,)

            self.groupsocks.append(s)
            print("Play connection est with: " + str(ip) + "    ",)

        while True:
            try:
                self.groupsocksready,_,_ = select.select(self.groupsocks, [], [])
            except:
                pass 