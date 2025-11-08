from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data store
todos = [
    {"id": 1, "task": "Learn TDD", "done": False},
    {"id": 2, "task": "Build a Flask API", "done": True},
]

@app.route('/')
def index():
    return "Welcome"

@app.route("/todos", methods=["GET"])
def get_todos():
    if request.method == "GET":
        return jsonify(todos)