import os
import json
from flask import Flask, jsonify, request
from flask_cors import CORS
from functions import mySql
from flask_jwt_extended import create_access_token, jwt_required, JWTManager
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes 
from cryptography.hazmat.primitives import padding 
import dotenv

dotenv.load_dotenv()
secretJWTKey = os.getenv("JWT_SECRET_KEY")

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = secretJWTKey
jwt = JWTManager(app)
CORS(app, supports_credentials=True)

# Funções
def generate_aes_key():
    aes_key = os.urandom(32)
    return aes_key

def encriptData(data, aes_key):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv))
    encryptor = cipher.encryptor()

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data.encode()) + padder.finalize()

    encrypted_bytes = encryptor.update(padded_data) + encryptor.finalize()
    return iv.hex(), encrypted_bytes.hex()

print(encriptData("Hello World!", generate_aes_key()))

# Rota para o login
@app.route('/api/login/', methods=['POST'])
def get_user():
    data = request.json

    result = mySql.showInformation("users", ("userName", "password"), "userName", data["user"])
    if not result:
        return jsonify({"message": "User not found"}), 404
    if result[0][0] == data["user"] and result[0][1] == data["password"]:
        return jsonify({"message": "Login successful"}), 200


# Rota para gerar uma chave AES-256 aleatório
@app.route("/api/get-aes-key", methods=["GET"])
def get_aes_key():
    aes_key = generate_aes_key()

if __name__ == "__main__":
    app.run(debug=True)
