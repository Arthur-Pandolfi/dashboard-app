import mysql.connector
import dotenv
import os

dotenv.load_dotenv()
database = os.getenv("DATABASE")
databaseUser = os.getenv("DATABASE_USER")
databasePassword = os.getenv("DATABASE_PASSWORD")
tables = os.getenv("TABLES")

def connect() -> None:
    return mysql.connector.connect(
        host="localhost",
        user=databaseUser,
        password=databasePassword,
        database=database
    )

def addInformationInTable(table: str, values: dict) -> str:
    connection = connect()
    cursor = connection.cursor()

    columns = ', '.join(values.keys())
    placeholders = ', '.join(['%s'] * len(values))

    if table in tables:
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
                
        try: 
            cursor.execute(query, tuple(values.values()))
            connection.commit()
        except mysql.connector.Error as error:
            print("Failed to insert record into table {}".format(error))
        finally:
            cursor.close()
            connection.close()
            return "Successfully added"
    else:
        exit("Table not found")

def showInformation(table: str, data: tuple, conditionColumn: str, conditionValue: str) -> list:
    connection = connect()
    cursor = connection.cursor()

    if table not in tables:
        exit("Table not found")
    else:
        columns = ', '.join(data)
        query = f"SELECT {columns} FROM {table} WHERE {conditionColumn} = {conditionValue}"

        cursor.execute(query)
        result = cursor.fetchall()
    
        cursor.close()
        connection.close()

    return result

def createTable(table: str, columns: tuple) -> None:
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table} ({columns}) DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci")
    cursor.close()
