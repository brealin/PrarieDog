import socket
from threading import Thread
from collections import deque
from Communication import Communication
from Server import Server

class Play(Thread,Communication):
# Maintains one connection to server and plays transmitted audio.   
    def __init__(self,cli):
        Thread.__init__(self)
        Communication.__init__(self)
        self.cli = cli
        self.frames = deque([],maxlen=self.PlyData.maxlen)         
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.buf = 0
        self.start()

    def run(self):
        while True:
            for ip,sock in self.cli.group.items():
                soundData, addr = sock.recvfrom(self.PlyData.maxlen)
                self.frames.append(soundData)
                self.Ply.write(self.frames.pop(), self.Ply._frames_per_buffer)
                                          
    def tcpStream(self):
        #TODO: while self.stream.is_active 
        while True:
            soundData, addr = self.s.recvfrom(self.frames.maxlen)
            self.frames.append(soundData)
    
        self.s.close()
    
    def ply(self):
        #TODO: while self.stream.is_active 
        while True:
            while len(self.frames) > self.buf:
                self.Ply.write(self.frames.pop(), self.Ply._frames_per_buffer)