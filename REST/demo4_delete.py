import mysql.connector

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "iotdb",
    use_pure = True
)

name = "rocky"

query = f"delete from persons where name = '{name}';"

cursor = connection.cursor()

cursor.execute(query)

connection.commit()

cursor.close()

connection.close()