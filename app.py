from flask import Flask, request, jsonify
from models import Schema
from service import ToDoService

app = Flask(__name__)


@app.route("/")
def hello():
    return "hello world!"


@app.route("/<name>")
def hello_name(name):
    return f"Hello {name}!"


@app.route("/todo", methods=["GET"])
def list_todo():
    return jsonify(ToDoService().list())


@app.route("/todo", methods=["POST"])
def create_todo():
    return jsonify(ToDoService().create(request.get_json()))


@app.route("/todo/<item_id>", methods=["PUT"])
def update_item(item_id):
    return jsonify(ToDoService().update(item_id, request.get_json()))


@app.route("/todo/<item_id>", methods=["DELETE"])
def delete_item(item_id):
    return jsonify(ToDoService().delete(item_id))


if __name__ == "__main__":
    Schema()
    app.run(debug=True)
