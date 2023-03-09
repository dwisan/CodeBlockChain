from wallet import Wallet
from transaction import Transaction
from mx_crypto import MxCrypto

wallet = Wallet(1024, True)
guy_wallet = Wallet(1024, True)

my_address = wallet.address
guy_address = guy_wallet.address

value = 10


def test_signature():
    # creation of a transaction with my wallet.
    transaction = Transaction(
        sender_address=my_address, recipient_address=guy_address, value=value)

    transaction.sign(wallet)

    assert transaction.verify_signature() == True

    # guy sign my transaction...
    transaction.sign(guy_wallet)
    is_valid = transaction.verify_signature()

    assert is_valid == False
