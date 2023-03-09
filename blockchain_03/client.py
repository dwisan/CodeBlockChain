from wallet import Wallet
from transaction import Transaction


class Client:
    def __init__(self):
        self.s = None

    @staticmethod
    def generate_transaction(wallet, recipient_address, value):
        if not isinstance(wallet, Wallet):
            raise ValueError('wallet param should be an instance of Wallet')

        # sender_address = request.form['sender_address']
        # recipient_address = request.form['recipient_address']
        # value = request.form['value']

        transaction = Transaction(
            wallet.address, recipient_address, value)

        transaction.sign(wallet)

        return transaction
