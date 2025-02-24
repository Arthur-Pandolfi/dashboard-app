import redis

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

def store_aes_key(user_id: int, expiration_time=int, aes_key=str) -> None:
    """
    Função para adicionar uma chave AES-256 ao banco de dados temporário KeyDB

    :param user_id: ID do usuário
    :param expiration_time: Tempo de expiração da chave AES-256 em segundos
    :param aes_key: Chave AES-256
    """
    connection = connect()

    connection.setex(f"aes_key:{user_id}", expiration_time, aes_key)

