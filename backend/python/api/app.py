from flask import Flask, jsonify, request
from flask_cors import CORS
from functions import mySql

app = Flask(__name__)
CORS(app)  # Permite acesso de outras origens (como o React)

# Rota para o login
@app.route('/api/login/', methods=['GET'])
def get_user():
    data = request.json
    

    mySql.showInformation("users", tuple(data.values()))
    return 200

if __name__ == "__main__":
    app.run(debug=True)