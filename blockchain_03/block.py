import jsonpickle
from time import time
import hashlib

MINING_DIFFICULTY = 2
HASH_GENESIS_BLOCK = "8f73145e22b5eef54041892ff92f7e1ab02d6c7246e76b81f0092a8adb13118e"


class Block(object):
    def __init__(self, nonce, transactions, index, previous_hash):
        self.index = index
        self.nonce = nonce
        self.transactions = transactions
        self.timestamp = time()
        self.previous_hash = previous_hash

    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a Block
        :param block: Block
        """

        if not isinstance(block, Block):
            raise ValueError(
                'block should be a Block instance but its .', type(block))

        # We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
        block_string = jsonpickle.encode(
            block).encode()

        # @TODO: algorithm of hash as class parameter.
        return hashlib.sha256(block_string).hexdigest()

    @staticmethod
    def valid_proof(prev_nonce, prev_hash, nonce, difficulty=MINING_DIFFICULTY):
        """
        Validates the Proof of work
        :param prev_nonce: <int> Previous Proof
        :param proof: <int> Current Proof
        :param prev_hash: <str> The hash of the Previous Block
        :return: <bool> True if correct, False if not.
        """

        if (prev_hash == HASH_GENESIS_BLOCK):
            return True

        guess = f'{prev_nonce}{nonce}{prev_hash}'.encode()

        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:difficulty] == '0'*difficulty

    @staticmethod
    def proof_of_work(last_block):
        """
        Simple Proof of Work Algorithm:
         - Find a number p' such that hash(pp') contains leading 4 zeroes
         - Where p is the previous proof, and p' is the new proof

        :param last_block: <dict> last Block
        :return: <int>
        """

        last_nonce = last_block.nonce
        last_hash = Block.hash(last_block)

        nonce = 0
        while Block.valid_proof(last_nonce, last_hash, nonce) is False:
            nonce += 1

        return nonce

    @staticmethod
    def valid_block(block_to_validate, previous_block):
        previous_block_hash = Block.hash(previous_block)

        if block_to_validate.previous_hash != previous_block_hash:
            print('block_to_validate.previous_hash != previous_block_hash')
            return False

        # Check that the Proof of Work is correct
        if not Block.valid_proof(previous_block.nonce, previous_block_hash, block_to_validate.nonce):
            print('Bad Proof of work. curr_nonce=',
                  block_to_validate.nonce, ' prev_nonce=', previous_block.nonce)
            return False

        return True

    def check_sender_stock(self, tx, nb):
        i = 1
        while 1 > nb and i <= len(self.transactions):
            if self.transactions[-i].value == tx.value:
                if self.transactions[-i].sender_address == tx.sender_address:
                    nb = nb - 1
                elif self.transactions[-i].recipient_address == tx.sender_address:
                    nb = nb + 1
            i = i + 1
        return nb
