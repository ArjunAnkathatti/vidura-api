#!/usr/bin/env python
from flask import Flask
from flask import jsonify
import JupyterNotebook as jn

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
   	data = {
	'hello' : 'world',
	'api-name': 'vidura-api',
	'api-version': 'V1'
	}

	resp = jsonify(data)
	resp.status_code = 200

	return resp

@app.route('/name')
def name():
	res = jn.get_string()
	data = {
	'response' : res
	}

	resp = jsonify(data)
	resp.status_code = 200

	return resp

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    response.headers.add('Content-type', 'application/json')
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
