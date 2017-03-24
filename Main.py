from Client import Client
from Server import Server
from Play import Play
from Broadcast import Broadcast
from Communication import Communication
from collections import deque
import socket
import pyaudio
#import netifaces

addr = input('Press enter to host. Otherwise, supply host address:  ',)

#Start one recording and one playing stream. Write record data to queue.
com = Communication(addr=addr)

#Start a group. One server thread, many client sockets.
if not (len(addr) > 0):
    Server()

#Join a group. One client thread, one server socket.
cli = Client()

#Start one broadcast thread, with many transmitting threads.
Broadcast()

#Start many play threads, each connected to one broadcast thread.
while True:
    if cli.new:
        Play(cli.new.pop())

#TODO: disoonnect from server
#TODO: disoonnect group
#TODO: exit