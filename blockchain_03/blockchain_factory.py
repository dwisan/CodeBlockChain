from blockchain import Blockchain
from network.network import Network


def blockchain_factory():
    """
    Create a new blockchain with its network.
    """
    network = Network()
    bc = Blockchain(network)

    network.set_blockchain(bc)

    return bc, network
