from threading import Thread
from AudioStream import AudioStream
from collections import deque
import socket
import copy
import itertools

class Broadcast(Thread,AudioStream):
#Broadcasts recording stream to every member address
    def __init__(self):
        Thread.__init__(self)
        AudioStream.__init__(self)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.settimeout(self.Tmt/2)
        self.start()

    def run(self):
        for ip,port in self.group.items():
            print('Broadcasting to '+ str(ip) +':'+str(port)+'    \r',)

        #TODO: while self.stream.is_active 
        while 1:
            if self.RecData:
                    #for ip,port in self.group.items():
                for ip,port in itertools.cycle(self.group.items()):
                    #frms = copy.copy(self.RecData) 
                    try:
                        self.s.sendto(self.RecData[0],(ip,port))
                    except socket.timeout as e:
                        print ('socket send timed out:  '+ip+':'+str(port)+' '+str(e),)
                        pass
        #self.Ply.stop_stream