import socket
from threading import Thread


class Node:
    """
    if host is none, so it's me -> auto discover of my local ip address.
    """

    def __init__(self, host_, myself=False):
        self.port = 5000
        self.my_socket = None
        self.host = host_

        if myself == True:
            print("I'm ready", self.host, ":", self.port)
            self._init_node()

    """
    Initialize the node as myself.
    """

    def _init_node(self):
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.my_socket.bind((self.host, self.port))

    def send(self, command_, node_, message_):
        
        if command_[:2] == "-a":
            #server = node_.host  # Server
            msg_to_send = (command_ + message_)
            #print('send msg:', msg_to_send, 'to ', node_)
            self.my_socket.sendto(msg_to_send.encode(), node_)
        
        else: 
            server = (node_.host, node_.port)  # Server
            msg_to_send = (command_ + message_)
            #print('send msg:', msg_to_send, 'to ', server)
            self.my_socket.sendto(msg_to_send.encode(), server)
