from flask import Flask, request

from utils.createResponse import create_response
from utils.executeSelectQuery import execute_select_query
from utils.executeQuery import execute_query

server = Flask(__name__)

@server.route('/', methods=['GET'])
def homepage():
    return create_response("This is home Page")

@server.route('/ldr',methods=['GET'])
def retrive_ldr():
    query = "select * from sensorLog where type = 'LDR';"
    values = execute_select_query(query)
    return create_response(values)

@server.route('/ldr',methods=['POST'])
def create_ldr():
    type = request.get_json().get('type')
    value = request.get_json().get('value')
    location = request.get_json().get('location')

    query = f"insert into sensorLog(type,value,location) values('{type}','{value}','{location}');"
    execute_query(query)

    return create_response("LDR reading is added successfully")

@server.route('/',methods=['PUT'])
def update_ldr():
    pass

@server.route('/ldr', methods =['DELETE'])
def delete_ldr():
    pass
@server.route('/lm35', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def lm35_ops():
    if request.method == 'GET':
        query = "select * from sensorLog where type = 'LM35';"
        values = execute_select_query(query)

        return create_response(values)
    
    elif request.method == 'POST':
        type = request.get_json().get('type')
        value = request.get_json().get('value')
        location = request.get_json().get('location')

        query = f"insert into sensorLog(type, value, location) values('{type}',{value},'{location}');"

        execute_query(query)
        return create_response("LM35 reading is added successfully")

    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass

if __name__ == '__main__':
    server.run(debug=True)    