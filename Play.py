import socket
from threading import Thread
from collections import deque
from Communication import Communication

class Play(Thread,Communication):
# Maintains one connection to server and plays transmitted audio.   
    def __init__(self,addr):
        Thread.__init__(self)
        Communication.__init__(self)
        self.BcstIp = addr
         #longer play queue than record queue. frames getting pushed off while trying to write to strm?
        self.frames = deque([],maxlen=self.PlyData.maxlen * 2)         
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.start()
        self.buf = 0

    def run(self):
        self.s.connect((self.BcstIp, self.StrmPort))
        self.Ts = Thread(target = self.tcpStream)
        self.Tp = Thread(target = self.ply,)
        self.Ts.start()
        self.Tp.start()
        print("Playing from: " + self.BcstIp + "...",)                
        #self.Ts.join()
        #self.Tp.join()

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