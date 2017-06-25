from threading import Thread
from AudioStream import AudioStream
import socket
from collections import deque
import select
import sys
import time
class Play(Thread,AudioStream):
#Recieves audio stream on socket   
    def __init__(self):
        Thread.__init__(self)
        AudioStream.__init__(self)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.settimeout(self.Tmt)
        self.buf = 2
        self.start()

    def run(self):
        self.s.bind((self.MyAddr,self.SrvrPort))
        self.Tp = Thread(target = self.ply,)
        self.Tp.start()
        print('Listening from '+ str(self.MyAddr) +':'+ str(self.SrvrPort)+'    \r',)


        while 1:
            try:
                soundData,address=self.s.recvfrom(self.Chk * self.RcvChk)
                self.PlyData.append(soundData)
                #print(len(str(self.PlyData)))
            except socket.timeout as e:
                print ('socket recv timed out:  \r'+ str(e),)
                pass


    def ply(self):
        #TODO: while self.stream.is_active
        time.sleep(2)
        while 1:
            sys.stdout.write("Buffering: %d%%   \r" % (round(len(self.PlyData)/(self.PlyData.maxlen if self.PlyData.maxlen > 0 else 1),2)*100))
            sys.stdout.flush()
            if (len(self.PlyData) > self.PlyData.maxlen/2):
                #while self.PlyData :
                    self.Ply.write(self.PlyData.pop(), self.Ply._frames_per_buffer)
        #self.Ply.stop_stream