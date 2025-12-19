# select max (salary) from employees;
# 1) SELECT MAX(salary) FROM employee;
# 2) SELECT salary FROM employee ORDER BY salary DESC LIMIT 1;
# 3) ## common table expression CTE
# WITH md AS 
# (SELECT salary FROM employee ORDER BY salary DESC LIMIT 1)
# SELECT * FROM md;

import mysql.connector
from flask import Flask, request
import mqtt_pub

mega_server = Flask(__name__)

def db_connection():
    return mysql.connector.connect(
        host = "127.0.0.1",
        port = 3306,
        user = "root",
        password = "root",
        database = "iotdb",
        use_pure = True
    )


#   i. /add - add user and health information into database table.

@mega_server.route('/')
def homepage():
    return "this is home page"

@mega_server.route('/add', methods = ['POST'])
def add_data():
    connection = db_connection()
    name = request.form.get('name')
    age = request.form.get('age')
    city = request.form.get('city')
    steps = request.form.get('steps')
    pulse = request.form.get('pulse')
    blood_oxygen = request.form.get('blood_oxygen')
    body_temperature = request.form.get('body_temperature')

    query = f"insert into fitness_tracker values('{name}',{age},'{city}',{steps},{pulse},{blood_oxygen},{body_temperature});"
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()

    if cursor.rowcount > 0:
        mqtt_pub.pub("/add", "success")
        result = "fitness details added successfully"
    else:
        mqtt_pub.pub("/add", "failure")
    cursor.close()
    connection.close()

    # return "fitness details added successfully"

# 	ii. /all - display health information of all users.
@mega_server.route('/all',methods = ['GET'])
def all_data():
    connection = db_connection()
    query = "select * from fitness_tracker;"
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    connection.close()

    if data:
        mqtt_pub.pub("/all","success")
    else:
        mqtt_pub.pub("/update", "failure")
    return f"persons = {data}"

# 	iii. /info - display health information of single user.
@mega_server.route('/info',methods=['GET'])
def single_info():
    connection = db_connection()
    name = request.form.get('name')
    query = f"select *  from fitness_tracker  where name ='{name}';"
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchone()
    cursor.close()
    connection.close()

    if data:
        mqtt_pub.pub("/info","success")
    else:
        mqtt_pub.pub("/update", "failure")
    return f"person = {data}"


# 	iv. /update - update city of given user.
@mega_server.route('/update', methods = ['POST'])
def update_data():
    connection = db_connection()
    name = request.form.get('name')
    city = request.form.get('city')

    query = f"update fitness_tracker SET city = '{city}' where name ='{name}';"
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()

    if cursor.rowcount > 0:
        mqtt_pub.pub("/update", "success")
        result = "city updated successfully"
    else:
        mqtt_pub.pub("/update", "failure")
        result = "user not found / city not updated"

    cursor.close()
    connection.close()



# 	v. /steps - display user information whose steps are maximum.
@mega_server.route('/steps',methods=['GET'])

def steps():
    connection = db_connection()
    query = "SELECT * FROM fitness_tracker WHERE steps = (SELECT MAX(steps) FROM fitness_tracker);"
    # query = "WITH md AS (SELECT * FROM fitness_tracker ORDER BY steps DESC LIMIT 1) SELECT * FROM md;"
    # query = "WITH md AS (SELECT MAX(steps) FROM fitness_tracker) SELECT * FROM md;"
    # WITH md AS (SELECT MAX(steps) FROM fitness_tracker) SELECT * FROM md; 

    # "SELECT * FROM fitness_tracker WHERE steps = (SELECT MAX(steps) FROM fitness_tracker)"

    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    connection.close()

    if data:
        mqtt_pub.pub("/steps","success")  
    else:
        mqtt_pub.pub("/update", "failure")  
    return f"person = {data}"

if __name__ == '__main__':
    mega_server.run(debug=True)


