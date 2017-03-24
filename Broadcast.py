import pyaudio
import socket
from threading import Thread
import time
from collections import deque
from Communication import Communication

class Broadcast(Thread,Communication):
# Maintains many client connections and transmits audio.   
    def __init__(self):
        Thread.__init__(self)
        Communication.__init__(self)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
        #self.daemon = True
        self.start()

    def run(self):
        self.s.bind((self.MyAddr, self.StrmPort))                      # Bind to the port

        #TODO: while self.stream.is_active 
        while True:
            clientsock = None
            self.s.listen()                                             # Now wait for client connection. THIS WILL QUEUE THE MAX SUPPLIED.
            clientsock, newAddr = self.s.accept()                       # Establish connection with client.
            Ts = Thread(target = self.tcpStream, args = (clientsock,))
            Ts.start()
            print("Broadcasting to: " + newAddr[0] + "...",)                
            #self.Ts.join()

        time.sleep(1)

    def tcpStream(self, clientsock):
        #TODO: while self.stream.is_active 
        while True:
            frm = self.RecData

            while len(frm) > 0:
                clientsock.send(frm.pop())
    
        self.s.close()