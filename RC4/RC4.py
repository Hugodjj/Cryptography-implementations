from KSA import KSA
from PRGA import PRGA

def RC4(key, data):
    """RC4 Implementation"""
    S = KSA(key)
    keystream = PRGA(S)
    return bytes([b ^ next(keystream) for b in data])