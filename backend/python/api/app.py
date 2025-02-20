from flask import Flask, jsonify, request
from flask_cors import CORS
from functions import mySql

app = Flask(__name__)
CORS(app)

# Rota para o login
@app.route('/api/login/', methods=['POST'])
def get_user():
    data = request.json

    result = mySql.showInformation("users", ("userName", "password"), "userName", data["user"])
    print(result)

    if result[0][0] == data["user"] and result[0][1] == data["password"]:
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid username or password"}), 401

if __name__ == "__main__":
    app.run(debug=True)