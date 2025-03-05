import redis
import json

def connect() -> redis.Redis:

    """Função para se conecter ao keyDB"""
    try:
        connection = redis.Redis(
            host="localhost",
            port=6379,
            db=0,
            decode_responses=True
        )
    except redis.exceptions.ConnectionError as e:
        print("Error in KeyDB Connection")
        print(e)
        exit()

    return connection

def store_loginInfos(ip: str, login_ID: str, aes_key: str, expiration_time: int) -> None:
    """
    Função para adicionar o IP do usuario, o ID de seu Login e sua chave AES-256-CBC ao banco de dados temporário KeyDB

    :param ip: IP do usuário
    :param login_ID: o ID do login do Usuário
    :param aes_key: Chave AES-256-CBC
    :param expiration_time: Tempo de expiração da chave AES-256 em segundos
    """

    connection = connect()
    infosToStore = {
        "ip": ip,
        "aes_key": aes_key
        }

    connection.setex(f"loginInfos:{login_ID}", expiration_time, json.dumps(infosToStore))

def get_loginInfos(login_ID: str):
    """
    Função para obter o IP do usuario, o ID de seu Login e sua chave AES-256-CBC do banco de dados temporário KeyDB

    :param login_ID: o ID do login do Usuário
    """
    connection = connect()
    data = connection.get(f"loginInfos:{login_ID}")
    return json.loads(data) if data else None
