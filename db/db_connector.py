import mysql.connector

def connect_to_db():
    return mysql.connector.connect(
    host='localhost',
    database = 'my_database',
    user='root',
    password='secretpswrd1'
    )
