from AudioStream import AudioStream
from Play import Play
from Broadcast import Broadcast
import time

#Start one recording and one playing stream. Write record data to queue.
strm = AudioStream()

#Start one broadcast thread, broadcasting recording stream to every member address.
brd = Broadcast()

#Start one play thread, recieving audio stream on socket.
ply = Play()
ply.join()

#TODO: disoonnect
#TODO: exit