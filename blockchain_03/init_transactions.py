from transaction import Transaction
import hashlib
from init_datas import creator_address
from init_datas import tx_signatures
from init_datas import time

#from wallet import Wallet
#creator_wallet = Wallet(); creator_address = creator_wallet.address; print(creator_address)

def getInitialTransactions():
    txs = []
    appleHash = hashImg('./items/apple.png')
    ironAxeHash = hashImg('./items/iron_axe.png')
    ironSwordHash = hashImg('./items/iron_sword.png')

    for i in range(4):
        tx = Transaction('', creator_address, appleHash)
        tx.signature = bytes.fromhex(tx_signatures[i*3])
        tx.time = time
        #tx.sign(creator_wallet); print("sign#", i*3, tx.signature.hex())
        txs.append(tx)

        tx = Transaction('', creator_address, ironAxeHash)
        tx.signature = bytes.fromhex(tx_signatures[i*3 + 1])
        tx.time = time
        #tx.sign(creator_wallet); print("sign#", i*3 + 1, tx.signature.hex())
        txs.append(tx)

        tx = Transaction('', creator_address, ironSwordHash)
        tx.signature = bytes.fromhex(tx_signatures[i*3 + 2])
        tx.time = time
        #tx.sign(creator_wallet); print("sign#", i*3 + 2, tx.signature.hex())
        txs.append(tx)

    return txs
 
def hashImg(img_path):
    img_content = _getImgData(img_path)
    return hashlib.sha256(img_content.encode()).hexdigest()  

def _getImgData(img_path):
    tmp = open(img_path, 'rb').read().hex()
    return tmp
