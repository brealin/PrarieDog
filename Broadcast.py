from threading import Thread
from Communication import Communication

class Broadcast(Thread,Communication):
# Maintains many client connections and transmits audio.   
    def __init__(self,srv):
        Thread.__init__(self)
        Communication.__init__(self)
        self.srv = srv
        #self.daemon = True
        self.start()

    def run(self):
        #TODO: while self.stream.is_active 
        while True:
            if self.RecData:
                for sock in self.srv.clients:
                    frm = self.RecData
                    while frm:
                        sock.send(frm.pop())                          