from KSA import KSA
from PRGA import PRGA


class RC4:
    def __init__(self, key,data):
        self.key = key
        self.data = data
    
    def RC4(key, data):
        """RC4 Implementation"""
        S = KSA(key)
        keystream = PRGA(S)
        return bytes([b ^ next(keystream) for b in data])
    
    def PRGA(S_box):
        """Pseudo-Random Generation Algorithm (PRGA)"""
        i = 0
        j = 0
        while True:
            i = (i + 1) % 256
            j = (j + S_box[i]) % 256
            S_box[i], S_box[j] = S_box[j], S_box[i]  # Troca S_box[i] e S_box[j]
            key = S_box[(S_box[i] + S_box[j]) % 256]
            yield key
            
    def KSA(key):
        """Key-Scheduling Algorithm (KSA)"""
        key_lengh = len(key)
        S_box = list(range(256))
        j = 0
        
        for i in range(256):
            j = (j + S_box[i] + key[i % key_lengh]) % 256
            S_box[i], S_box[j] = S_box[j], S_box[i]  # Troca S_box[i] e S_box[j]
        
        return S_box