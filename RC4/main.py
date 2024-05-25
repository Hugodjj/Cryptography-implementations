from create_read_file import read_sample_file as readfile
from create_read_file import create_sample_file as createfile
from RC4 import RC4

# Function to convert string into list of ASCII values
def string_to_bytes(s):
    return [ord(c) for c in s]

# Function to convert a list of ASCII values into a string
def bytes_to_string(b):
    return ''.join([chr(x) for x in b])

def main():
    # Create a sample file
    sample_file_name = 'RC4_Sample.txt'
    sample_content = "SOCORRAM-ME SUBI NO ONIBUS EM MARROCOS."
    createfile(sample_file_name, sample_content)

    # Defining key and text and transforming into bytes
    key = "key"
    text = readfile(sample_file_name)
    key_bytes = string_to_bytes(key)
    text_bytes = string_to_bytes(text)

    # Encrypting
    cipher_text_bytes = RC4(key_bytes, text_bytes)
    ciphertext = bytes_to_string(cipher_text_bytes)
    createfile("RC4_Cipher_Text.txt",ciphertext)

    # Decrypting
    decrypted_text_bytes = RC4(key_bytes, cipher_text_bytes)
    decrypted_text = bytes_to_string(decrypted_text_bytes)
    createfile("RC4_Decrypted_Text.txt",decrypted_text)

main() 