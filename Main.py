from Communication import Communication
from Client import Client
from Server import Server
from Play import Play
from Broadcast import Broadcast
from collections import deque
import socket
import pyaudio
#import netifaces

addr = input('Press enter to host. Otherwise, supply host address:  ',)

#Start one recording and one playing stream. Write record data to queue.
com = Communication(addr=addr)

#Start a group. One server thread. Inherits comm data and maintains sockets.
host = False
if not (len(addr) > 0):
   host = True
#TODO: implement host and non host logic
srv = Server(host)

#Join a group. One client thread. Inherits com data, recieves group meta from srv and maintains a sock to each.
cli = Client()

#Start one broadcast thread. Inherits client group and creates outgoing stream to each sock.
brd = Broadcast(srv)

#Start one play thread. Inherits client group and merges incoming stream from each sock.
ply = Play(cli)
#ply.join()

#TODO: disoonnect from server
#TODO: disoonnect group
#TODO: exit