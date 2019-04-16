import json
from flask import Flask
from flask import jsonify
import requests

app = Flask(__name__)

@app.route('/api/pokemon/<int:num>')
def index(num):
	data = {}

	URL = "https://pokeapi.co/api/v2/pokemon/"
	URL = URL + str(num)
	response = requests.get(url = URL)
	responseData = response.json()
	data['id'] = responseData['id']
	data['name'] = responseData['name']
	data['sprite'] = responseData['sprites']['back_default']
	pokemon = {}
	pokemon['pokemon'] = data
	json_data = json.dumps(pokemon)

	return json_data


if __name__ == '__main__':
    app.run(port=8006)