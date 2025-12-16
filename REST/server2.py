from flask import Flask

server = Flask(__name__)

@server.get('/')
def homepage():
    return "<html> <body> <h1> This is home page </h1> </body> </html>"

@server.get('/welcome')
def welcome():
    return "<html> <body> <h1> Welcome to IoT Application </h1></body></html>"

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug = True)