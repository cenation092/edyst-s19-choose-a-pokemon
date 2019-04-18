import json
from flask import Flask, render_template

app = Flask(__name__)

# error handler for invalid url
@app.errorhandler(404)
def page_not_found_404(e):
    return render_template('404.html'), 404

# routing for display pokemon data
@app.route('/api/pokemon')
def index():
	data = {} # dictionary for storing pokemon's data
	name = ["bulbasaur", "charmander", "squirtle"]
	data['pokemon'] = name
	json_data = json.dumps(data) # convert data into JSON format
	return json_data

if __name__ == '__main__':
    app.run(port=8006)