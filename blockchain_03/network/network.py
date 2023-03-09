import socket
import jsonpickle
import threading
from network.node import Node


class Network:

    def __init__(self):
        self.node = Node("192.168.1.82", True)
        self.nodes = []
        self.blockchain = None

        # Thread management
        self._running = True
        self.t1 = threading.Thread(target=self.receiv)
        self.t1.start()
        self._broadcast_ping()

    def stop(self):
        self._running = False

    def set_blockchain(self, blockchain_):  # Done
        self.blockchain = blockchain_

    def broadcast_transaction(self, str_transaction_):  # Done
        for nodeList in self.nodes:
            self.node.send("-t ", nodeList, str_transaction_)

    def broadcast_block(self, str_block_):  # Done
        for nodeList in self.nodes:
            self.node.send("-b ", nodeList, str_block_)

    def broadcast_ask_chain(self):  # Done
        for nodeList in self.nodes:
            self.node.send("-c ", nodeList, "")

    def _broadcast_ping(self): #Not use
        nodeBroadcast = Node("192.168.1.62")
        myNodeToSend = jsonpickle.encode(self.node)
        self.node.send("-p ", nodeBroadcast, myNodeToSend)

    def receiv(self):
        print("ready to receiv")

        while self._running is True:
            data, addr = self.node.my_socket.recvfrom(4096)

            cureNode = addr

            myData = data.decode()

            if myData[:3] == "-c ":  # Done
                # Retourne le JSON de la chaine
                self.node.send("-ac", cureNode, self.blockchain.chain_for_network)

            elif myData[:3] == "-n ":  # Done
                print("I received a Node")
                # Parcourir la liste de noeud et les envois a l'emmeteur
                for nodeList in self.nodes:
                    nodeToSend = jsonpickle.encode(nodeList)
                    self.node.send("-an", cureNode, nodeToSend)

            elif myData[:3] == "-t ":  # Done
                # Reception d'une transaction
                self.blockchain.submit_transaction(myData[3:len(myData)])

            elif myData[:3] == "-b ":  # Done
                # Reception d'un block
                self.blockchain.submit_block(myData[3:len(myData)])

            elif myData[:3] == "-p ":  # Done
                print('Ping received')
                # Repond present
                nodeToSend = jsonpickle.encode(self.node)
                self.node.send("-ap", cureNode, nodeToSend)

                nodeReceiv = jsonpickle.decode(myData[3:len(myData)])
                print("Try to add node : ", nodeReceiv.host)

                notFind = True
                for nodeList in self.nodes:
                    if nodeList.host == nodeReceiv.host:
                        notFind = False

                if notFind:
                    print("Connecting to a new Node: ", nodeReceiv.host)
                    self.nodes.append(nodeReceiv)
                    notFind = False

            elif myData[:3] == "-ac":  # En suspend
                some = None

            elif myData[:3] == "-ap":  # Done
                nodeReceiv = jsonpickle.decode(myData[3:len(myData)])

                print("Try to add node : ", nodeReceiv.host)

                notFind = True
                for nodeList in self.nodes:
                    if nodeList.host == nodeReceiv.host:
                        notFind = False

                if notFind:
                    print("Connecting to a new Node: ", nodeReceiv.host)
                    self.nodes.append(nodeReceiv)
                    notFind = False
