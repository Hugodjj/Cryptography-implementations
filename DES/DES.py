import pyDes

class DES3Cryptor:
    def __init__(self, key):
        if len(key) not in [8, 16, 24]:
            raise ValueError("Invalid key size, key must be 8, 16, or 24 bytes long.")
        self.key = key

    def encrypt(self, data, triple_des):
        if triple_des:
            des = pyDes.triple_des(self.key, pyDes.CBC, self.key[:8], pad=None, padmode=pyDes.PAD_PKCS5)
        else:
            des = pyDes.des(self.key, pyDes.CBC, self.key, pad=None, padmode=pyDes.PAD_PKCS5)
        return des.encrypt(data)

    def decrypt(self, data, triple_des):
        if triple_des:
            des = pyDes.triple_des(self.key, pyDes.CBC, self.key[:8], pad=None, padmode=pyDes.PAD_PKCS5)
        else:
            des = pyDes.des(self.key, pyDes.CBC, self.key, pad=None, padmode=pyDes.PAD_PKCS5)
        return des.decrypt(data)

    def encrypt_file(self, file_path, output_path, triple_des):
        with open(file_path, 'rb') as f:
            data = f.read()
        encrypted_data = self.encrypt(data, triple_des=triple_des)
        with open(output_path, 'wb') as f:
            f.write(encrypted_data)

    def decrypt_file(self, file_path, output_path, triple_des):
        with open(file_path, 'rb') as f:
            data = f.read()
        decrypted_data = self.decrypt(data, triple_des=triple_des)
        with open(output_path, 'wb') as f:
            f.write(decrypted_data)