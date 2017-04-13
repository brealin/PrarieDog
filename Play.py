from threading import Thread
from Communication import Communication
import socket
from collections import deque

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
        self.Tp = Thread(target = self.ply,)
        self.Tp.start()

        while True:
            for sock in self.cli.groupsocksready:
                soundData, addr = sock.recvfrom(self.PlyData.maxlen)
                self.frames.append(soundData)
                #self.Ply.write(soundData, self.Ply._frames_per_buffer)

    def ply(self):
        #TODO: while self.stream.is_active 
        while True:
            while len(self.frames) > self.buf:
                self.Ply.write(self.frames.pop(), self.Ply._frames_per_buffer)