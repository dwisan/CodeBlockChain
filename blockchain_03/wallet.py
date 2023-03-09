from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5
from Crypto import Random
from base64 import b64encode, b64decode
import hashlib
from Crypto.Hash import SHA256
from mx_crypto import MxCrypto
from transaction import Transaction


class Wallet:
    """
    Manage my priv/pub key.
    """

    def __init__(self, key_length=4096, regenerate=False, testDatas=False):
        if regenerate is True:
            public_key, private_key = MxCrypto.generate_keys(key_length)
        else:
            if testDatas is True:
                try:
                    public_key, private_key = Wallet._import_keys('./testKeys/')
                except FileNotFoundError:
                    raise ValueError('Test keys not found, please import it')
            else:
                try:
                    public_key, private_key = Wallet._import_keys()
                except FileNotFoundError:
                    print("ERROR : Keys not found - Generate new keys")
                    # to handle!
                    public_key, private_key = MxCrypto.generate_keys(key_length)

                    Wallet._save_key(public_key, private_key)


        self.public_key = public_key
        self.private_key = private_key

        self.address = self.public_key.export_key().decode()

        # self.address = hashlib.sha256(
        #     str_public_key.encode('utf-8')).hexdigest()

    @staticmethod
    def _save_key(public_key, private_key):
        # Converting the RsaKey objects to string
        private_pem = private_key.export_key().decode()
        public_pem = public_key.export_key().decode()

        # Writing down the private and public keys to 'pem' files
        with open('./keys/private.pem', 'w') as pr:
            pr.write(private_pem)
        with open('./keys/public.pem', 'w') as pu:
            pu.write(public_pem)

    @staticmethod
    def _import_keys(path = './keys/'):
        """
        Importing keys from files, converting it into the RsaKey object
        """
        private_key = RSA.import_key(open(path + 'private.pem', 'r').read())

        str_public_key = open(path + 'public.pem', 'r').read()
        public_key = RSA.import_key(str_public_key)

        return public_key, private_key

    def sign_transaction(self, transaction):
        """
        Sign transaction with private key
        """

        # if not isinstance(transaction, Transaction):
        #     raise ValueError('transaction should be Transation instance.')

        return MxCrypto.sign(self.private_key, transaction)
