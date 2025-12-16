
import mysql.connector

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "iotdb",
    use_pure = True
)

uid = 8
name = "indra"
age = 34
address = "chennai"
mobile = 1234654352

query = f"insert into persons values({uid},'{name}',{age}, '{address}','{mobile}')"

cursor = connection.cursor()

cursor.execute(query)

connection.commit()

cursor.close()
connection.close()