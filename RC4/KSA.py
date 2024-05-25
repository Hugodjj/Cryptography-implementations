def KSA(key):
    """Key-Scheduling Algorithm (KSA)"""
    key_lengh = len(key)
    S_box = list(range(256))
    j = 0
    
    for i in range(256):
        j = (j + S_box[i] + key[i % key_lengh]) % 256
        S_box[i], S_box[j] = S_box[j], S_box[i]  # Troca S_box[i] e S_box[j]
    
    return S_box