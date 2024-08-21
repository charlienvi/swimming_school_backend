from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Load JSON data
def load_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Save JSON data
def save_data(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

# Load persons and addresses data
persons_data = load_data('data/persons.json')
addresses_data = load_data('data/addresses.json')

# CRUD Operations for Persons
@app.route('/persons', methods=['GET'])
def get_persons():
    return jsonify(persons_data)

@app.route('/persons/<int:person_id>', methods=['GET'])
def get_person(person_id):
    person = next((p for p in persons_data['persons'] if p['id'] == person_id), None)
    if person:
        return jsonify(person)
    return jsonify({'message': 'Person not found'}), 404

@app.route('/persons', methods=['POST'])
def create_person():
    new_person = request.json
    persons_data['persons'].append(new_person)
    save_data('persons.json', persons_data)
    return jsonify(new_person), 201

@app.route('/persons/<int:person_id>', methods=['PUT'])
def update_person(person_id):
    person = next((p for p in persons_data['persons'] if p['id'] == person_id), None)
    if person:
        for key, value in request.json.items():
            person[key] = value
        save_data('persons.json', persons_data)
        return jsonify(person)
    return jsonify({'message': 'Person not found'}), 404

@app.route('/persons/<int:person_id>', methods=['DELETE'])
def delete_person(person_id):
    global persons_data
    persons_data['persons'] = [p for p in persons_data['persons'] if p['id'] != person_id]
    save_data('persons.json', persons_data)
    return jsonify({'message': 'Person deleted'}), 200

# CRUD Operations for Addresses
@app.route('/addresses', methods=['GET'])
def get_addresses():
    return jsonify(addresses_data)

@app.route('/addresses/<int:address_id>', methods=['GET'])
def get_address(address_id):
    address = next((a for a in addresses_data['addresses'] if a['id'] == address_id), None)
    if address:
        return jsonify(address)
    return jsonify({'message': 'Address not found'}), 404

@app.route('/addresses', methods=['POST'])
def create_address():
    new_address = request.json
    addresses_data['addresses'].append(new_address)
    save_data('addresses.json', addresses_data)
    return jsonify(new_address), 201

@app.route('/addresses/<int:address_id>', methods=['PUT'])
def update_address(address_id):
    address = next((a for a in addresses_data['addresses'] if a['id'] == address_id), None)
    if address:
        for key, value in request.json.items():
            address[key] = value
        save_data('addresses.json', addresses_data)
        return jsonify(address)
    return jsonify({'message': 'Address not found'}), 404

@app.route('/addresses/<int:address_id>', methods=['DELETE'])
def delete_address(address_id):
    global addresses_data
    addresses_data['addresses'] = [a for a in addresses_data['addresses'] if a['id'] != address_id]
    save_data('addresses.json', addresses_data)
    return jsonify({'message': 'Address deleted'}), 200

if __name__ == '__main__':
    app.run()
