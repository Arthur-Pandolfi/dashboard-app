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

    # Transforma o dado criptografado em bytes, captura o IV e os dados criptografados
    encrypted_data_bytes = bytes.fromhex(encrypted_data)
    iv = encrypted_data_bytes[:16] # Pega os primeiros 16 bytes (IV)
    encrypted_message = encrypted_data_bytes[16:] # Pega os bytes restantes (Dados criptografados)

    # Cria o objeto descriptografador usando a chave AES-256-CBC e transforma a chave AES em bytes
    aes_key_bytes = bytes.fromhex(aes_key)
    cipher = Cipher(algorithms.AES(aes_key_bytes), modes.CBC(iv))
    decryptor = cipher.decryptor()
    decrypted_padded = decryptor.update(encrypted_message) + decryptor.finalize()

    # Remover o Padding (espaço adicionado no texto para completar o bloco de 16 bytes)
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    decryptted_data = unpadder.update(decrypted_padded) + unpadder.finalize()

    return decryptted_data.decode("utf-8")

