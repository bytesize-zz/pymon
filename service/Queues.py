# using TCP/IP
from socket import socket, AF_INET, SOCK_STREAM


def askForRepaint(inst):
     print('hi from Queue', inst)
     for idx in range(10):
         inst.gui_queue.put('Message from a queue: ' + str(idx))
     inst.create_thread(6)