import pyaudio
import time
import socket
from collections import deque

class AudioStream(object):
    class __Singleton:
        def __init__(self, addr):
            self.talk = time.time() + 2
            self.group = {}
            self.MyName = socket.gethostname()
            self.MyAddr = socket.gethostbyname(self.MyName)
            try:
                netifaces.ifaddresses('wlan0')
                self.MyAddr = netifaces.ifaddresses('wlan0')[2][0]['addr']
            except:
                pass
            self.SrvrPort = 8000
            self.Chn = 1
            self.Rt = 6000
            self.Chk = 2048
            self.Tmt = 6
            self.RcvChk = len(self.group.keys()) if len(self.group.keys()) > 1 else 2
            self.Fmt = pyaudio.paInt16
            with open('member.config','r') as file:
                for line in file:
                    x = line.index(':')
                    ip = line[0:x]
                    port = line[x+1:]
                    port = port.strip('\n')
                    if (ip == str(self.MyAddr)):
                        self.SrvrPort = int(port)
                    else:
                        self.group[ip]=int(port)
            self.RecData = deque([],maxlen=1 * self.Chn * 2)
            self.PlyData = deque([],maxlen=1 * self.Chn * len(self.group.keys()) * 16)
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
                         stream_callback=self.RecCallback
                         )
            self.Rec.start_stream

        def RecCallback(self,in_data,frame_count,time_info,status):
            self.RecData.append(in_data)           
            return (in_data, pyaudio.paContinue)

    instance = None

    def __init__(self, **kwargs):
        if not AudioStream.instance:
            AudioStream.instance = AudioStream.__Singleton(kwargs.get('addr'))

    def __getattr__(self, name):
        return getattr(self.instance, name)
