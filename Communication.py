import pyaudio
import socket
from collections import deque

class Communication(object):
    class __Singleton:
        def __init__(self, addr):
            self.MyName = socket.gethostname()
            self.MyAddr = socket.gethostbyname(self.MyName)
            try:
                netifaces.ifaddresses('wlan0')
                self.MyAddr = netifaces.ifaddresses('wlan0')[2][0]['addr']
            except:
                pass
            self.SrvrPort = 8000
            self.Chn = 1
            self.Rt = 8000
            self.Chk = 512
            self.Fmt = pyaudio.paInt16
            self.RecData = deque([],maxlen=self.Chk * self.Chn * 2)
            self.PlyData = deque([],maxlen=self.Chk * self.Chn * 2)
            p = pyaudio.PyAudio()  
            self.Ply = p.open(format=self.Fmt,
                        channels=self.Chn,
                        rate=self.Rt,
                        output=True,
                        frames_per_buffer=self.Chk
                        #stream_callback=pCallback
                        )
            self.Rec = p.open(format=self.Fmt,
                         channels=self.Chn,
                         rate=self.Rt,
                         input=True,
                         frames_per_buffer=self.Chk,
                         stream_callback=self.RecCallback)
            self.Rec.start_stream
            self.group = {}
            with open('member.config','r') as f:
                for line in f:
                    x = line.index(':')
                    ip = line[0:x]
                    port = line[x+1:]
                    port = port.strip('\n')
                    if (ip == str(self.MyAddr)):
                        self.SrvrPort = int(port)
                    else:
                        self.group[ip]=int(port)

        def RecCallback(self,in_data,frame_count,time_info,status):
            self.RecData.append(in_data)
            return (in_data, pyaudio.paContinue)

    instance = None

    def __init__(self, **kwargs):
        if not Communication.instance:
            Communication.instance = Communication.__Singleton(kwargs.get('addr'))

    def __getattr__(self, name):
        return getattr(self.instance, name)