from block import Block
from blockchain import Blockchain


def test_proof_of_work():
    blockchain = Blockchain()
    blockchain.mine()

    assert len(blockchain.chain) == 2

    prev_block = blockchain.chain[0]
    prev_hash = Block.hash(prev_block)

    curr_block = blockchain.chain[-1]

    proof = Block.valid_proof(prev_block.nonce, prev_hash, curr_block.nonce)

    assert proof == True

    blockchain.mine()

    prev_block = blockchain.chain[1]
    prev_hash = Block.hash(prev_block)
    curr_block = blockchain.chain[-1]

    proof = Block.valid_proof(prev_block.nonce, prev_hash, curr_block.nonce)

    assert proof == True
