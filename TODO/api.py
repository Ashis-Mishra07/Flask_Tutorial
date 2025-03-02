# Here We Will learn the PUT and DELETE method 
# Working with API also get performed

from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy Data -> Initial data for my todo list

items = [
    {
        'id': 1,
        'name': 'Do Homework',
        'description': "This is item1"
    },
    {
        'id': 2,
        'name': 'Do Laundry',
        'description': "This is item2"
    }
]



@app.route('/')
def home():
    return "Welcome to the sample TODO list app"

# GET Method -> Retrieve all the items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# GET Method -> Retrieve a single item ny id
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item_by_id(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({'message': 'Item not found'}), 404


# POST : create a new task
@app.route('/items', methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({'message': 'Bad request'})  , 404
     
    new_item = {
        'id': items[-1]['id'] + 1,
        'name': request.json['name'],
        'description': request.json.get('description', '')
    }
    items.append(new_item)
    return jsonify(new_item), 201


# PUT : Update a task
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({'message': 'Item not found'}), 404
    
    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])
    
    return jsonify(item)


# DELETE : Delete a task
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({'message': 'Item deleted'})


if __name__ == '__main__':
    app.run(debug=True)

