import CryptoJS from "crypto-js";

export function encryptData(data, aes_key) {
    /**
     * Função para criptografar os dados usando AES-256 CBC
     * 
     * @param {string} data - Dados a serem criptografados 
     * @param {string} aes_key - Chave AES-256
     * @returns {Object} - Objeto contendo o IV e o dado criptografado
     */ 
    const iv = CryptoJS.lib.WordArray.random(16);
    const key = CryptoJS.enc.Hex.parse(aes_key);
    const encrypted = CryptoJS.AES.encrypt(data, key, {
        iv: iv,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    });
    
    return {
        encryptedData: iv.toString(CryptoJS.enc.Hex) + encrypted.ciphertext.toString(CryptoJS.enc.Hex)
    }
}
