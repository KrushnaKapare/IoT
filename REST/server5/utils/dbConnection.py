import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        password = "root",
        database = "iotdb",
        use_pure = True
    )
    return connection