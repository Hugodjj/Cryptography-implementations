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