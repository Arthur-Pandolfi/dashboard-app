from flask import Flask, jsonify, request
from flask_cors import CORS
from functions import mySql

app = Flask(__name__)
CORS(app)  # Permite acesso de outras origens (como o React)

# Rota para o login
@app.route('/api/login/request', methods=['POST'])
def get_user():
    dados = request.json
    return dados, 200

def returnUserPermission() -> str:
    pass


if __name__ == "__main__":
    app.run(debug=True)