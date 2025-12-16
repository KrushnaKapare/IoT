import mysql.connector

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "iotdb",
    use_pure = True
)

cursor = connection.cursor()

query = "SELECT * from persons;"

cursor.execute(query)

data = cursor.fetchall()

for person in data:
    print(person)

cursor.close()

connection.close()