import os
import json
import dotenv
from functions import keyDb
from functions import mySql
from flask_cors import CORS
from datetime import timedelta
from functions import encryption
from flask import Flask, jsonify, request
from cryptography.hazmat.primitives import padding 
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes 
from flask_jwt_extended import create_access_token, jwt_required, JWTManager

dotenv.load_dotenv()
secretJWTKey = os.getenv("JWT_SECRET_KEY")

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = secretJWTKey
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=2)
jwt = JWTManager(app)
CORS(app, supports_credentials=True)

# Rota para o login
@app.route('/api/login/', methods=['POST'])
def get_user():
    data = request.json
    expirationTime = 10 #7200

    result = mySql.showInformation("users", ("id", "userName", "password"), "userName", data["user"])
    if not result:
        return jsonify({"message": "User not found"}), 404
    if result[0][1] == data["user"] and result[0][2] == data["password"]:
        aes_key = encryption.generate_aes_key()
        acces_token = create_access_token(identity=data["user"], additional_claims={"aes_key": aes_key.hex()})
        keyDb.store_aes_key(result[0][0], expirationTime, aes_key.hex())

        return jsonify(
            {
                "message": "Login successful",
                "token": acces_token
            }
        ), 200


# Rota para gerar uma chave AES-256 aleatório
@app.route("/api/get-aes-key", methods=["GET"])
def get_aes_key():
    aes_key = encryption.generate_aes_key()
    return jsonify(
        {
            "aes_key": aes_key.hex()
        }
    ), 200

if __name__ == "__main__":
    app.run(debug=True)
