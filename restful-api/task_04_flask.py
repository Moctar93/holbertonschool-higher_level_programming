from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory storage for users
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def data():
    # Return a list of usernames
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    # Return a simple status message
    return "OK"

@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    # Return the user data for the given username
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    # Add a new user to the users dictionary
    if not request.json:
        abort(400, description="Invalid input")
    
    data = request.json
    username = data.get('username')
    
    if username in users:
        return jsonify({"error": "User already exists"}), 400
    
    user = {
        "username": username,
        "name": data.get('name'),
        "age": data.get('age'),
        "city": data.get('city')
    }
    
    users[username] = user
    return jsonify({"message": "User added", "user": user}), 201

if __name__ == "__main__":
    app.run(debug=True)

