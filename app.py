from flask import Flask, request, jsonify

app= Flask(__name__)

users = {}

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/users', methods=['POST'])
def create_user():
    data= request.get_json()
    user_id = data.get('id')
    name= data.get('name')
    
    if not user_id or not name:
        return jsonify({"error": "ID and name are required"}), 400

    if user_id in users:
        return jsonify({"error": "User already exists"}), 409

    users[user_id] = {"id": user_id, "name": name}
    return jsonify(users[user_id]), 201

@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    name = data.get('name')

    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    
    users[user_id]['name']= name
    return jsonify({'message': 'User updated successfully'}), 200
    