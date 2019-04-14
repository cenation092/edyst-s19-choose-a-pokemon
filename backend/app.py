import json
from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/api/pokemon')
def index():
	data = {}
	name = ["bulbasaur", "charmander", "squirtle"]
	data['pokemon'] = name
	json_data = json.dumps(data)
	return json_data

if __name__ == '__main__':
    app.run(port=8006)