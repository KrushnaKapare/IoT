from flask import jsonify

def create_response(msg, error = False):
    d = dict()
    if error == True:
        d = {
            'Response code' : '?',
            'Response string' : '?',
            'extra MSG' : msg
        }
    else:
        d = {
            'Response code' : '200',
            'Response string' : 'OK',
            'Extra Data/Msg' : msg
        }

        return jsonify(d)