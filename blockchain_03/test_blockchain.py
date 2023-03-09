from blockchain import Blockchain
from wallet import Wallet
from client import Client
from init_transactions import hashImg
from transaction import Transaction

from init_datas import creator_address

blockchain = Blockchain()

wallet = Wallet()
guy_wallet = Wallet(1024, True)

def test_submit_transaction():
    transaction = Client.generate_transaction(
        wallet, guy_wallet.address, 10)

    # don't forget genesis block
    assert len(blockchain.current_transactions) == 0
    blockchain.submit_transaction(transaction)
    assert len(blockchain.chain) == 1


def test_mine():
    for i in range(10):
        transaction = Client.generate_transaction(
            wallet, guy_wallet.address, 10)
        blockchain.submit_transaction(transaction)

    print(blockchain.mine())


def test_chain_for_network():
    for i in range(3):
        transaction = Client.generate_transaction(
            wallet, guy_wallet.address, 10)
        blockchain.submit_transaction(transaction)

    blockchain.mine()

    s = blockchain.chain_for_network
    assert isinstance(s, str) == True


def test_valid_chain():
    s = blockchain.chain_for_network
    valid = blockchain.valid_chain(s)

    assert valid == True

def test_check_sender_stock():
    testWallet = Wallet(testDatas=True)
    appleHash = hashImg('./items/apple.png')

    tx = Transaction(guy_wallet.address, creator_address, appleHash)
    assert blockchain.check_sender_stock(tx) == False

    txAB = Transaction(creator_address, guy_wallet.address, appleHash)
    assert blockchain.check_sender_stock(txAB) == True

    txBA = Transaction(guy_wallet.address, creator_address, appleHash)
    assert blockchain.check_sender_stock(txBA) == False

    txAB.sign(testWallet)
    if blockchain.submit_transaction(txAB):
        assert blockchain.check_sender_stock(txBA) == True
