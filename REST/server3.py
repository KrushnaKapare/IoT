
from flask import Flask

app = Flask(__name__)

@app.get('/')
def homepage():
    return "This is home page"

@app.get('/temperatures')
def get_temperatures():
    temps = [35.2, 23.3, 21.2, 10.4]

    return f"temps = {temps}"

@app.post('/temperature/<float:temp>')
def post_temperature(temp):
    print(f"Recived Temp : {temp}")

    return f"{temp} is receied successfully"

if __name__ == '__main__':
    app.run(debug=True)