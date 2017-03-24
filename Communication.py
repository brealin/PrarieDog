import pyaudio
import socket
#import netifaces
from collections import deque

class Communication(object):
    class __Singleton:
        def __init__(self, addr):
            self.MyName = socket.gethostname()
            self.MyAddr = socket.gethostbyname(self.MyName)
            self.SrvrAddr = addr
            if not self.SrvrAddr:
                self.SrvrAddr = ''
            try:
                netifaces.ifaddresses('wlan0')
                self.MyAddr = netifaces.ifaddresses('wlan0')[2][0]['addr']
            except:
                pass
            if not(len(self.SrvrAddr) > 0):
                self.SrvrAddr = self.MyAddr        
            self.StrmPort = 9000
            self.SrvrPort = 8000
            self.Chn = 1
            self.Rt = 8000
            self.Chk = 1024
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

        def RecCallback(self,in_data,frame_count,time_info,status):
            self.RecData.append(in_data)
            return (in_data, pyaudio.paContinue)

    instance = None

    def __init__(self, **kwargs):
        if not Communication.instance:
            Communication.instance = Communication.__Singleton(kwargs.get('addr'))

    def __getattr__(self, name):
        return getattr(self.instance, name)