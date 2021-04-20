from flask import Blueprint
from app.models.task import Task
from flask import request, Blueprint, make_response

task_bp = Blueprint("task", __name__, url_prefix="/tasks")

@task_bp.route("/hello_world", methods=["GET", "POST", "PUT", "DELETE"])
def tasks():
    if request.method == "POST":
        request_body = request.get_json()
        new_task = Task(
            title=request_body["title"],
            description=request_body["description"],
            completed_at=None
        )
        db.session.add(new_task)
        db.session.commit()

        if not new_task:
            return_response = make_response(
                {"details": "Invalid data"}, 400)
        else:
            return_response = make_response(new_task.make_json(), 201)


        return return_response

    elif request.method == "GET":
        tasks = Task.query.all()
        tasks_response = []
        for task in taskss:
            tasks_response.append(task.make_json())
        
        return_response = make_response(tasks_response, 200)

        return return_response




