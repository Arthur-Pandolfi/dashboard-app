import os
import json
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

# Rotas do keyDB
# Rota para gerar uma chave AES-256-CBC aleatória e armazenar na KeyDB
@app.route("/api/keyDB/get-and-store-aes-key", methods=["POST"])
def get_aes_key():
    aes_key = encryption.generate_aes_key()
    data = request.json
    keyDb.store_loginInfos(data["ip"], data["loginID"], aes_key.hex(), 40)
    return jsonify(
        {
            "aes_key": aes_key.hex()
        }
    ), 200

# Rotas de Login
# Rota para gerar o ID do login
@app.route("/api/login/generate-id", methods=["GET"])
def generate_id_login():
    return jsonify(
        {
            "id_login": str(uuid.uuid4())
        }
    ), 200

# Rota para checar se o IP ja está logado
@app.route("/api/login/ip-alredy-logged", methods=["POST"])
def ip_already_logged():
    data = request.json
    ip = data['ip']
    userLogged = keyDb.get_loged_ip(ip)

    if userLogged:
        token = keyDb.get_loged_ip(ip)[1]
        return jsonify({
            "logged": "true",
            "token": token
        }), 200
    else:
        return jsonify({"logged": "false"})


# Rota para o login
@app.route('/api/login/submit-login', methods=['POST'])
def submit_login():
    data = request.json
    dataToDecrypt = data["data"]["encryptedData"]
    loginInfos = keyDb.get_loginInfos(data["loginId"])
    aes_key = loginInfos["aes_key"]
    decryptedData = encryption.decryptData(dataToDecrypt, aes_key)
    decryptedData = json.loads(decryptedData)
    
    try:
        result = mySql.showInformationWithWhere("users", ("id", "userName", "password"), "userName", "test")
        if result[0][1] == decryptedData["user"] and result[0][2] == decryptedData["password"]:
            acces_token = create_access_token(identity=decryptedData["user"], expires_delta=timedelta(hours=2))
            keyDb.store_loged_ip(data["ip"], acces_token, result[0][0], keyDB_store_time_duration)
            return jsonify(
                {
                    "message": "Login successful",
                    "token": acces_token
                }
            ), 200
        else:
            raise Exception
    except Exception as error:
        return jsonify({
                "message": "User not found",
                "error": str(error)
            }), 202
    
# Rota para mostrar as informações
@app.route('/api/home/getInformations', methods=['POST'])
def getInformations():
    data = request.json
    ip = data["ip"]
    data = keyDb.get_loged_ip_data(ip)
    userID = data["userID"]

    if data == "User has no data":
        print("no data")
        return jsonify({"message": "User has no data"}), 202
    try:
        result = mySql.showInformation(f"informations{userID}", ("*"))

        dataToReturn = {
            "id": result[0],
            "name": result[1],
            "body": result[2]
        }
        return jsonify(dataToReturn), 200
    except Exception as error:
        print(error)
        print('my sql error')
        return jsonify({"message": "Error in mySql"}), 204

if __name__ == "__main__":
    app.run(debug=True)
