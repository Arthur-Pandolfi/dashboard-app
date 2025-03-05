import os
import base64
from cryptography.hazmat.primitives import padding 
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes 

def generate_aes_key():
    """
    Função para gerar uma chave AES-256-CBC aleatória e armazenar na KeyDB
    
    :return: Chave AES-256-CBC
    """
    aes_key = os.urandom(32)
    return aes_key

def decryptData(encrypted_data: str, aes_key: str):
    """
    Função para descriptografar informações criptografadas usando AES-256-CBC
    
    :param encrypted_data: Dados criptografados
    :param aes_key: Chave AES-256-CBC

    :return: Dados descriptografados
    """

    encrypted_data_bytes = base64.b64decode(encrypted_data)

print(decryptData("5c858275d6f4b39f3226a0ff76f5773892c3f0e28aeab434e95935c233d57257a4cc5aa32ae6f9cd9fb33b013ff640b5", "aes_key"))