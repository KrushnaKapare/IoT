
import mysql.connector
from flask import Flask, request

mega = Flask(__name__)

def db_connection():
    return mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "iotdb",
    use_pure = True
)

@mega.get('/')
def homepage():
    return "this is home page"


@mega.route('/employees', methods=['GET'])
def get_employee():
    connection = db_connection()
    query = "select  * from employees;"
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()

    return f" employees = {data}"
    
    

@mega.route('/employees',methods = {'POST'})
def add_employee():
    connection = db_connection()
    empid = request.form.get('empid')
    name  = request.form.get('name')
    department = request.form.get('department')
    email = request.form.get('email')
    salary  = request.form.get('salary')
    joining_date = request.form.get('joining_date')

    query = f"insert into employees values({empid},'{name}','{department}','{email}',{salary},{joining_date});"
   
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()

    return "employee details added successfully"

@mega.route('/employees',methods=['PUT'])
def update_employee():
    connection = db_connection()

    empid = request.form.get('empid')
    name  = request.form.get('name')
  
    query = f"update employees SET name ='{name}' where empid ={empid};"

    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()

    return f" name of employee with empid = {empid} is updated succesfully"

@mega.route('/employees',methods=['DELETE'])
def delete_employee():
    connection = db_connection()
    empid = request.form.get('empid')
    query = f" delete from employees where empid = {empid};"

    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()

    return f"employee with empid {empid} is deleted successfully"

# * In program add web services to print all employees,
# employees of given department, employee with highest and lowest salary

@mega.route('/employees/all',methods = ['GET'])
def all_employee():
    connection = db_connection()
    query = f"select * from employees;"
    
    cursor = connection.cursor()
    cursor.execute(query)
    cursor.execute(query)
    data = cursor.fetchall()
    return f"employees = {data}"

@mega.route('/employees/department/<string:department>',methods = ['GET'])
def employee_by_department(department):
    connection = db_connection()
    query = f"select * from employees where department = '{department}';"
    
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    return f"employees = {data}"

@mega.route('/employees/highest-salary', methods=['GET'])
def highest_salary():
    connection = db_connection()
    query = "select * from employees order by salary desc limit 1;"
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchone()
    cursor.close()
    connection.close()

    return f"highest salary employee details {data}"

@mega.route('/employees/lowest-salary', methods=['GET'])
def lowest_salary():
    connection = db_connection()
    query = "select * from employees order by salary asc limit 1;"
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchone()
    cursor.close()
    connection.close()

    return f"lowest salary employee details {data}"

if __name__ == '__main__':
    mega.run(debug=True)