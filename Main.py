from Communication import Communication
from Client import Client
from Server import Server
from Play import Play
from Broadcast import Broadcast
from collections import deque
import socket
import pyaudio
#import netifaces

#Start one recording and one playing stream. Write record data to queue.
com = Communication()
srv = Server()

#Join a group. One client thread. Inherits com data, recieves group meta from srv and maintains a sock to each.
cli = Client()

#Start one broadcast thread. Inherits client group and creates outgoing stream to each sock.
brd = Broadcast(srv)

#Start one play thread. Inherits client group and merges incoming stream from each sock. Don't continue until disconnect.
ply = Play(cli)
ply.join()

#TODO: disoonnect from server
#TODO: disoonnect group
#TODO: exit