#!/usr/bin/python3
"""
A simple Flask API with endpoints to get and add users.
"""

from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

# Users stored in-memory
users = {
    # Example: "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"}
}

@app.route("/", methods=["GET"])
def home():
    """Root endpoint."""
    return "Welcome to the Flask API!"


@app.route("/status", methods=["GET"])
def status():
    """Check API status."""
    return "OK"


@app.route("/data", methods=["GET"])
def get_usernames():
    """Return a list of all usernames."""
    return jsonify(list(users.keys()))


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """Return full object for a specific username."""
    user = users.get(username)
    if user:
        return jsonify(user)
    return make_response(jsonify({"error": "User not found"}), 404)


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user from JSON payload."""
    if not request.is_json:
        return make_response(jsonify({"error": "Invalid JSON"}), 400)

    data = request.get_json()

    username = data.get("username")
    if not username:
        return make_response(jsonify({"error": "Username is required"}), 400)

    if username in users:
        return make_response(jsonify({"error": "Username already exists"}), 409)

    # Save user
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return make_response(jsonify({"message": "User added", "user": users[username]}), 201)


if __name__ == "__main__":
    app.run()
