from blockchain_factory import blockchain_factory
from wallet import Wallet
from transaction import Transaction
import time


bc, network = blockchain_factory()

time.sleep(5)

wallet = Wallet()
wallet2 = Wallet(1024, True)
transaction = Transaction(wallet.address, wallet2.address, "bonjour")
transaction2 = Transaction(wallet.address, wallet2.address, "bonjour2")
transaction3 = Transaction(wallet.address, wallet2.address, "bonjour3")

transaction.sign(wallet)

bc.submit_transaction(transaction)
bc.submit_transaction(transaction2)
bc.submit_transaction(transaction3)