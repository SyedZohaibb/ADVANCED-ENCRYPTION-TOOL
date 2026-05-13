from Crypto.Cipher import AES

def decrypt_file(file_path):

    # Read saved key
    with open("secret.key", "rb") as key_file:
        key = key_file.read()

    # Read encrypted file
    with open(file_path, "rb") as file:
        nonce = file.read(16)
        tag = file.read(16)
        ciphertext = file.read()

    # Create cipher object
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)

    # Decrypt file
    data = cipher.decrypt_and_verify(ciphertext, tag)

    # Remove .enc extension
    output_file = file_path.replace(".enc", "")

    # Save decrypted file
    with open(output_file, "wb") as file:
        file.write(data)

    return output_file