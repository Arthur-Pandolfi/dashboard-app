# import secrets

# jwt_secret = secrets.token_hex(32)

# print(jwt_secret)

from functions import keyDb

keyDb.store_loginInfos("127.0.0.1", "1", "1", 10)
