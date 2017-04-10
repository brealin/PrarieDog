import socket
import select
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
            for sock in self.cli.groupsocksready:
                soundData, addr = sock.recvfrom(self.PlyData.maxlen)
                self.Ply.write(soundData, self.Ply._frames_per_buffer)