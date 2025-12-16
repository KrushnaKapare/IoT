import mysql.connector

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "iotdb",
    use_pure = True
)

uid = 9 
name = "rocky"
age = 30
address = "delhi"
mobile = "9191121377"

query = f"insert into persons values({uid}, '{name}',{age},'{address}','{mobile}');"

cursor = connection.cursor()

cursor.execute(query)

connection.commit()
cursor.close()

connection.close()