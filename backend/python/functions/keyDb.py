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
    dataToStore = {
        "ip": ip,
        "aes_key": aes_key
        }

    connection.setex(f"loginInfos:{login_ID}", expiration_time, json.dumps(dataToStore))
    connection.close()

def get_loginInfos(login_ID: str):
    """
    Função para obter o IP do usuario, o ID de seu Login e sua chave AES-256-CBC do banco de dados temporário KeyDB

    :param login_ID: o ID do login do Usuário
    """
    connection = connect()
    data = connection.get(f"loginInfos:{login_ID}")
    connection.close()

    return json.loads(data) if data else None

def store_loged_ip(ip: str, acces_token: str, userID: int,  expiration_time: int) -> None:
    """
    Função para adicionar o IP do usuário, seu accesToken e chave AES-256-CBC ao banco de dados temporário KeyDB

    :param ip: IP do usuário
    :param acces_token: acces token do Usuário
    :param expiration_time: Tempo de expiração do acces token em segundos
    :param userID: ID do Usuário
    """
    
    connection = connect()
    print("Connection success")
    dataToStore = {
        "accesToken": acces_token,
        "userID": userID
    }

    connection.setex(f"logedIP:{ip}", expiration_time, json.dumps(dataToStore))
    connection.close()


def get_loged_ip_data(ip: str) -> dict:
    """
    Função para obter as informações sobre um usuário que tem seu IP logado

    :param ip: IP do usuário

    :return: Dados do usuário
    """

    connection = connect()
    data = connection.get(f"logedIP:{ip}")
    connection.close()

    if data is not None:
        jsonData = json.loads(data)
        return jsonData
    else:
        return "User has no data"

def get_loged_ip(ip: str) -> bool:
    """
    Função para obter se o IP do usuário ja esta logado

    :param ip: IP do usuário
    """

    connection = connect()
    data = connection.get(f"logedIP:{ip}")
    connection.close()

    if data is not None:
        jsonData = json.loads(data)
        return True, jsonData['accesToken']
    else:
        return False
