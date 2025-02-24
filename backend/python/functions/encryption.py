import os
from cryptography.hazmat.primitives import padding 
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes 

def generate_aes_key():
    aes_key = os.urandom(32)
    return aes_key

def decryptData():
    pass