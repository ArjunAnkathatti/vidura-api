#!/bin/python
from flask import Flask
from flask import Response
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    data = {
	'hello' : 'world',
	'api-name': 'vidura-api',
	'api-version': 'V1'
    }

    resp = jsonify(data)
    resp.status_code = 200

    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
