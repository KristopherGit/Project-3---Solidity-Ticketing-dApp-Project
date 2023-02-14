# UsePass Login / Hashing SubRoutine
# AES encryption program - symmetric encryption (password_hash_tester)
# user password entered to hash all data that will be displayed in the blockchain's metadata

import base64
import hashlib
from cryptography.fernet import Fernet


def encrypt_url(url, password):
    salt = b'_salt_'
    kdf = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    key = base64.urlsafe_b64encode(kdf)
    cipher_suite = Fernet(key)
    encrypted_url = cipher_suite.encrypt(url.encode())
    return encrypted_url


def decrypt_url(encrypted_url, password):
    salt = b'_salt_'
    kdf = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    key = base64.urlsafe_b64encode(kdf)
    cipher_suite = Fernet(key)
    decrypted_url = cipher_suite.decrypt(encrypted_url)
    return decrypted_url.decode()


#url = "https://gateway.pinata.cloud/ipfs/bafybeigdc5imvtpgx6n3y5wmzj7jgzflulkfgfcdonaufzotdp5rgpiljy"
#password = "icelandsaga101"

#encrypted_url = encrypt_url(url, password)
#decrypted_url = decrypt_url(encrypted_url, password)

#print("Encrypted URL:", encrypted_url)
#print("Decrypted URL:", decrypted_url)
