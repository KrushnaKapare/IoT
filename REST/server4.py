
from flask import Flask, request
import mysql.connector

mega = Flask("__name__")

@mega.get('/')
def jestson():
    return "This is Jetson Nano"

@mega.route('/person',methods=['GET'])
def get_persons():
    connection = mysql.connector.connect(
        host = 'localhost',
        port = 3306,
        user = "root",
        password = "root",
        database = "iotdb",
        use_pure = True
    )

    query = "select * from persons;"
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    connection.close
    return f"persons = {data}"

@mega.route('/person',methods=['POST'])
def post_person():
    uid = request.form.get('uid')
    name = request.form.get('name')
    age = request.form.get('age')
    address = request.form.get('address')
    mobile = request.form.get('mobile')

    connection2 = mysql.connector.connect(
        host = 'localhost',
        port = 3306,
        user = "root",
        password = "root",
        database = "iotdb",
        use_pure = True
    )

    query = f"insert into persons values({uid},'{name}',{age},'{address}','{mobile}');"

    print(query)
    cursor = connection2.cursor()
    cursor.execute(query)
    connection2.commit()
    cursor.close()
    connection2.close()

    return "Person details are added successfully"

@mega.route('/person', methods=['PUT'])
def update_person():
    uid = request.form.get('uid')
    address = request.form.get('address')
    
    query = f"update persons SET address = '{address}' where uid ={uid};"

    connection3 = mysql.connector.connect(
        host = 'localhost',
        port = 3306,
        user = "root",
        password = "root",
        database = "iotdb",
        use_pure = True
    )
    cursor = connection3.cursor()
    cursor.execute(query)
    connection3.commit()
    cursor.close()
    connection3.close()

    return f"address of person with uid = {uid} is updated successfully"

@mega.route('/person', methods =['DELETE'])
def delete_person():
    uid = request.form.get('uid')

    query = f"delete from persons where uid = {uid};"
    
    connection4 = mysql.connector.connect(
        host = 'localhost',
        port = 3306,
        user = "root",
        password = "root",
        database = "iotdb",
        use_pure = True
    )

    cursor = connection4.cursor()
    cursor.execute(query)
    connection4.commit()
    cursor.close()
    connection4.close()

    return f"person with uid {uid} is deleted successfully"

if __name__ == '__main__':
    mega.run(debug=True)