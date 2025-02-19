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

def showInformation(table: str) -> dict:
    pass

addInformationInTable("teste", {"id": 3, "nome": "Alice"})
