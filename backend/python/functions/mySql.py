import mysql.connector
import dotenv
import os

dotenv.load_dotenv()
database = os.getenv("DATABASE")
databaseUser = os.getenv("DATABASE_USER")
databasePassword = os.getenv("DATABASE_PASSWORD")
tables = os.getenv("TABLES")
waranty_message = os.getenv("WARANTY_MESSAGE")

def connect() -> None:
    """
    Função para se conectar ao banco de dados MySql
    
    :return Conexão ou Erro de conexão
    """
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user=databaseUser,
            password=databasePassword,
            database=database
        )
        return connection 
    except Exception as error:
        print("Error in MySql Connection")
        print(error)
        raise Exception

def addInformationInTable(table: str, values: dict) -> str:
    """
    Função para adicionar informaçãos em uma tabela

    :param table: Nome da tabela
    :param values: Valores que serão adicionados na tabela

    :return: Estado da operação como String
    """
    try:
        connection = connect()
        cursor = connection.cursor()
        print("MySql Connection Success!")
    except Exception as error:
        print("Error in MySql Connection")
        print(error)
        raise Exception

    columns = ', '.join(values.keys())
    placeholders = ', '.join(['%s'] * len(values))

    if table in tables:
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders});"
                
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

def showInformation(table: str, data: tuple) -> list:
    """
    Função para obter informações de uma tabela

    :param table: Nome da tabela
    :param data: Uma tupla com as coulunas

    :return: Uma tupla com os resultados
    """
    try:
        connection = connect()
        cursor = connection.cursor()
        print("MySql Connection Success!")
    except Exception as error:
        print("Error in MySql Connection")
        print(error)
        raise Exception

    if table not in tables:
        print('Table not found')
        raise Exception
    else:
        print('Searching infos')
        columns = ', '.join(data)
        query = f"SELECT {columns} FROM {table};"
        print("Infos searched with success") 

        cursor.execute(query)
        result = cursor.fetchall()
    
        cursor.close()
        connection.close()

    return result[0]

def showInformationWithWhere(table: str, columns: tuple, conditionColumn: str, conditionValue: str) -> list:
    """
    Função para obter informações de uma tabela com uma condição

    :param table: Nome da tabela
    :param columns: Uma tupla com as coulunas
    :param conditionColumn: Nome da coluna da condição
    :param conditionValue: Valor da condição

    :return: Uma tupla com os resultados
    """
    
    try:
        connection = connect()
        cursor = connection.cursor()
    except Exception as error:
        print("Error in MySql Connection")
        print(error)
        raise Exception

    if table not in tables:
        print("Table not found")
        raise Exception
    else:
        formatedColumns = ', '.join(columns)
        query = f"SELECT {formatedColumns} FROM {table} WHERE {conditionColumn} = '{conditionValue}';"

        cursor.execute(query)
        result = cursor.fetchall()
    
        cursor.close()
        connection.close()

    return result[0]

def createTable(table: str, columns: tuple) -> None:
    """
    Função para criar uma tabela no MySql

    :param table: Nome da tabela
    :param columns: Uma tupla com as coulunas

    :return: None
    """
    try:
        connection = connect()
        cursor = connection.cursor()
        print("MySql Connection Success!")
    except Exception as error:
        print("Error in MySql Connection")
        print(error)
        raise Exception
    
    formatedColumns = ', '.join(columns)
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table} ({formatedColumns}) DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci")
    cursor.close()

def dropTable(table: str, waranty: str) -> None:
    """
    Função para deletar uma tabela no MySql

    :param table: Nome da tabela
    :param waranty: Informação de garantia

    :return: None
    """
    try:
        connection = connect()
        cursor = connection.cursor()
        print("MySql Connection Success!")
    except Exception as error:
        print("Error in MySql Connection")
        print(error)
        raise Exception

    if waranty == waranty_message:
        cursor.execute(f"DROP TABLE IF EXISTS {table}")
        connection.commit()
    else:
        print("Table not dropped, waranty information not provided")
        raise Exception
    connection.close()
    cursor.close()
