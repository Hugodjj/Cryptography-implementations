from DES import DES3Cryptor
from create_read_file import create_sample_file


def main():
    # Create a sample file
    sample_file_name = 'DES_Sample.txt'
    encrypted_file_name = 'DES_Encrypted.txt'
    decrypted_file_name = 'DES_Decrypted.txt'
    sample_content = "SOCORRAM-ME SUBI NO ONIBUS EM MARROCOS."
    create_sample_file(sample_file_name, sample_content)
    
    # Initializing the DES3Cryptor with a 24-byte key for 3DES
    key_3DES = b"1234567890abcdef12345678"  # key for DES (8 bytes)
    key_8_bytes = b"12345678"  # key for 3DES (24 bytes)
    cryptor = DES3Cryptor(key_3DES)

    
    # Encrypting
    cryptor.encrypt_file(sample_file_name, encrypted_file_name, triple_des=True)
    
    # Decrypting
    cryptor.decrypt_file(encrypted_file_name, decrypted_file_name, triple_des=True)

main()