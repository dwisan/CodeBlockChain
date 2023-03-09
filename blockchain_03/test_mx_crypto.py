from base64 import b64encode, b64decode
from mx_crypto import MxCrypto

public_key, private_key = MxCrypto.generate_keys(1024)

attack_public_key, attack_private_key = MxCrypto.generate_keys(1024)


def test_decrypt():
    msg = b"hello world!"
    encrypted = MxCrypto.encrypt(public_key, msg)
    original = MxCrypto.decrypt(private_key, encrypted)

    assert msg == original


def test_sign():
    msg = "Hello world!"

    signature = MxCrypto.sign(private_key, msg)
    verify = MxCrypto.verify(public_key, msg, signature)

    altered_msg = b"Hello woorld!"
    altered_verify = MxCrypto.verify(public_key, altered_msg, signature)

    # I verify with another pub_key (pub_key doesn't correspond to priv_key that have created this signature).
    fake_verify = MxCrypto.verify(attack_public_key, msg, signature)

    assert verify == True
    assert altered_verify == False
    assert fake_verify == False
