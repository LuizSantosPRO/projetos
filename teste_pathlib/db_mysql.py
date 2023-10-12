import mysql.connector
from mysql.connector import Error
# import numpy
# import pandas as pd


def criar_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database sucesso na connecção")
    except Error as err:
        print(f"Error: '{err}'")
    return connection


def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")


pw = "Las2023@01MySQL"  # senha do root do MySQL
db = "scholl"          # nome do banco de dados que será criado

connection = criar_server_connection("localhost", "root", pw)
create_database_query = "CREATE DATABASE school"
create_database(connection, create_database_query)
