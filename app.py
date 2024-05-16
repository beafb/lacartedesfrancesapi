from flask import Flask, jsonify, make_response, url_for
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-type'


@app.route('/')
@cross_origin()
def home():
	r = {"message":  "Bonjour"}
	
	with app.open_resource('static/points.json') as f:
		data = json.load(f)

	ret = make_response(data)
	ret.mimetype = 'application/json'
	return ret


@app.route('/tacos')
@cross_origin()
def tacos():
	with app.open_resource('static/tacos.json') as f:
		data = json.load(f)
	ret = make_response(data)
	ret.mimetype = 'application/json'
	return ret


if __name__ == '__main__':
	app.run(debug=True)