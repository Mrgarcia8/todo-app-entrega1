from flask import Flask, jsonify, request

app = Flask(__name__)

# --------------------------
#  MODELO DE TAREAS (MEMORIA)
# --------------------------
tasks = []
task_id_counter = 1


# --------------------------
#  RUTA PRINCIPAL
# --------------------------
@app.route("/")
def home():
    return {"message": "Todo App funcionando correctamente"}


# --------------------------
#  OBTENER TODAS LAS TAREAS
# --------------------------
@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)


# --------------------------
#  CREAR UNA TAREA
# --------------------------
@app.route("/tasks", methods=["POST"])
def create_task():
    global task_id_counter

    data = request.json
    new_task = {
        "id": task_id_counter,
        "title": data.get("title", ""),
        "completed": False
    }

    tasks.append(new_task)
    task_id_counter += 1

    return jsonify({"message": "Tarea creada", "task": new_task}), 201


# --------------------------
#  ACTUALIZAR UNA TAREA
# --------------------------
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            data = request.json
            task["title"] = data.get("title", task["title"])
            task["completed"] = data.get("completed", task["completed"])
            return jsonify({"message": "Tarea actualizada", "task": task})

    return jsonify({"error": "Tarea no encontrada"}), 404


# --------------------------
#  ELIMINAR UNA TAREA
# --------------------------
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks

    tasks = [task for task in tasks if task["id"] != task_id]

    return jsonify({"message": "Tarea eliminada"})


# --------------------------
#  INICIALIZAR APP
# --------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

