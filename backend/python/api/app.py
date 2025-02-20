from flask import Flask, jsonify, request
from flask_cors import CORS
from functions import mySql

app = Flask(__name__)
CORS(app, supports_credentials=True)

# Rota para o login
@app.route('/api/login/', methods=['POST'])
def get_user():
    data = request.json

    result = mySql.showInformation("users", ("userName", "password"), "userName", data["user"])
    if not result:
        return jsonify({"message": "User not found"}), 404
    if result[0][0] == data["user"] and result[0][1] == data["password"]:
        return jsonify({"message": "Login successful"}), 200

if __name__ == "__main__":
    app.run(debug=True)
