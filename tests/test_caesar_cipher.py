from caesar_cipher.caesar_cipher import *

def test_encrypt():
    assert encrypt('helloo',5) == 'mjqqtt'


def test_decrypt():
    assert decrypt('mjqqtt',5) == 'helloo'


def test_crack():
    assert crack('stuj65') == 'nope10'