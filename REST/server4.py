
from flask import Flask, request
import mysql.connector

app = Flask(__name__)

@app.get('/')
def homepage():
    return "This is home page"

@app.route('/persons', methods=['GET'])
def get_persons():
    conn = mysql.connector.connect(
        host = 'localhost',
        port = 3306,
        user = "root",
        password = "root",
        database = "iotdb",
        use_pure = True
    )

    