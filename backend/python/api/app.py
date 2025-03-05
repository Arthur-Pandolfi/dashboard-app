import os
import uuid
import dotenv
from functions import keyDb
from functions import mySql
from flask_cors import CORS
from datetime import timedelta
from functions import encryption
from flask import Flask, jsonify, request 
from flask_jwt_extended import create_access_token, jwt_required, JWTManager

dotenv.load_dotenv()
secretJWTKey = os.getenv("JWT_SECRET_KEY")
keyDB_store_time_duration = os.getenv("KEYDB_STORE_TIME_DURATION")

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = secretJWTKey
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=2)
jwt = JWTManager(app)
CORS(app, supports_credentials=True)

# Rota para gerar uma chave AES-256-CBC aleatória e armazenar na KeyDB
@app.route("/api/keyDB/get-and-store-aes-key", methods=["POST"])
def get_aes_key():
    aes_key = encryption.generate_aes_key()
    data = request.json
    keyDb.store_loginInfos(data["ip"], data["loginID"], aes_key.hex(), 10)
    return jsonify(
        {
            "aes_key": aes_key.hex()
        }
    ), 200

# Rotas de Login
@app.route("/api/login/generate-id", methods=["GET"])
def generate_id_login():
    return jsonify(
        {
            "id_login": str(uuid.uuid4())
        }
    ), 200

# Rota para o login
@app.route('/api/login/submit-login', methods=['POST'])
def get_user():
    data = request.json

    print(data)
    exit()
    try:
        result = mySql.showInformation("users", ("id", "userName", "password"), "userName", data["user"])
        result[0][1] == data["user"] and result[0][2] == data["password"]
        return jsonify(
            {
                "message": "Login successful",
                # "token": acces_token
            }
        ), 200
    except mysql.connector.Error as error:
        return jsonify({"message": "User not found"}), 404

        # acces_token = create_access_token(identity=data["user"], additional_claims={"aes_key": aes_key.hex()})

       


if __name__ == "__main__":
    app.run(debug=True)
