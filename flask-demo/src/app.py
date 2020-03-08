from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
	{
		'name': 'store_1',
		'items': [
			{
				'name': 'item1',
				'price': 14.99
			},
		]
	},
]
# POST
# GET

@app.route('/')
def home():
	return render_template('index.html')

# POST /store data: {name}
@app.route('/store', methods=['POST'])
def create_store():
	request_data = request.get_json()
	for store in stores:
		if request_data['name'] == store['name']:
			return jsonify({'error': 'store exists'})
	new_store = {
		'name': request_data['name'],
		'items': []
	}
	stores.append(new_store)
	return jsonify(new_store)
	

# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
	for store in stores:
		if store['name'] == name:
			return jsonify(store)
	return jsonify({'error': 'store not found'})

# GET /store
@app.route('/store')
def get_stores():
	return jsonify({'stores': stores})

# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
	for store in stores:
		if store['name'] == name:
			request_data = request.get_json()
			store['items'].append({'name': request_data['name'], 'price': request_data['price']})
			return jsonify({'created': 'item appended'})
	return jsonify({'error': 'store not found'})

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
	for store in stores:
		if store['name'] == name:
			return jsonify({'items': store['items']})
	return jsonify({'error': 'not items to return'})			

app.run(port=5000)