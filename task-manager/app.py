from flask import Flask, request, jsonify
from tasks import add_task, get_tasks

app = Flask(__name__)

@app.route("/tasks", methods=["GET"])
def list_tasks():
    return jsonify(get_tasks())

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.json
    task = add_task(data["name"])
    return jsonify(task)

if __name__ == "__main__":
    app.run(debug=True)

def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete(task_id):
    delete_task(task_id)
    return {"status": "deleted"}
