from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

def encrypt_file(file_path):
    
    # Generate AES-256 key
    key = get_random_bytes(32)
    # Create cipher object
    cipher = AES.new(key, AES.MODE_EAX)

    # Open selected file
    with open(file_path, "rb") as file:
        data = file.read()

    # Encrypt data
    ciphertext, tag = cipher.encrypt_and_digest(data)

    # Create encrypted filename
    encrypted_file = file_path + ".enc"

    # Save encrypted data
    with open(encrypted_file, "wb") as file:
        file.write(cipher.nonce)
        file.write(tag)
        file.write(ciphertext)

    # Save key separately
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

    return encrypted_file