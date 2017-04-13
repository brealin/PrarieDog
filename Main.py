from Communication import Communication
from Client import Client
from Server import Server
from Play import Play
from Broadcast import Broadcast

#Start one recording and one playing stream. Write record data to queue.
com = Communication()

#Wait for connections from each group member, maintain server socket collection.
#TODO: do we need to maintain non-blocking server socket collection? - Does it even block until bytes are received?
srv = Server()

#Connect to each group member, maintain non-blocking client socket collection.
cli = Client()

#Start one broadcast thread, using server sockets. Wait until group is connected to limit threads.
srv.join()
brd = Broadcast(srv)

#Start one play thread, using client sockets. Join to prevent extra thread.
ply = Play(cli)
ply.join()
#TODO: disoonnect from server
#TODO: disoonnect group
#TODO: exit