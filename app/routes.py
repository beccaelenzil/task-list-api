from flask import Blueprint
from app import db
from app.models.task import Task
from flask import jsonify, request, Blueprint, make_response
import datetime
import requests
import os


task_bp = Blueprint("task", __name__, url_prefix="/tasks")

@task_bp.route("", methods=["GET", "POST"])
def tasks():
    if request.method == "POST":
        request_body = request.get_json()


        if ('title' not in request_body) or ('description' not in request_body) or ('completed_at' not in request_body):
            return make_response({"details": "Invalid data"}, 400)

        if request_body['completed_at']:
            the_time = request_body['completed_at']
        else:
            the_time = None


        new_task = Task(
            title=request_body['title'],
            description=request_body['description'],
            completed_at=the_time
        )
        db.session.add(new_task)
        db.session.commit()

        if not new_task:
            return_response = make_response(
                {"details": "Invalid data"}, 400)
        else:
            return_response = make_response(
                {'task': new_task.make_json()}, 201)


        return return_response

    elif request.method == "GET":

        sort_query = request.args.get("sort")
        if sort_query=="asc":
            tasks = Task.query.order_by(Task.title.asc())
        elif sort_query=="desc":
            tasks = Task.query.order_by(Task.title.desc())
        else:
            tasks = Task.query.all()

        tasks_response = []
        for task in tasks:
            tasks_response.append(task.make_json())
        
        return_response = make_response(jsonify(tasks_response), 200)

        print(return_response)
        
        return return_response


@task_bp.route("/<task_id>", methods=["GET", "PUT", "DELETE"])
def task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return make_response('',404)

    if request.method=="GET":
        return make_response({'task':task.make_json()}, 200)

    elif request.method=="PUT":
        
        request_body = request.get_json()

        if 'title' in request_body:
            task.title = request_body['title']
        if 'description' in request_body:
            task.description = request_body['description']

        db.session.commit()

        return make_response({'task': task.make_json()}, 200)

    elif request.method=="DELETE":
        db.session.delete(task)
        db.session.commit()
        return make_response({'details':f'Task {task.task_id} "{task.title}" successfully deleted'},200)

@task_bp.route("/<task_id>/mark_complete", methods=["PATCH"])
def mark_complete(task_id):
    task = Task.query.get(task_id)

    if not task:
        return make_response('',404)
    
    completed_at = task.completed_at
    task.completed_at = datetime.datetime.utcnow()
    db.session.commit()

    # if not completed_at:
    #     requests.post("https://slack.com/api/chat.postMessage",
    #     data={
    #         "token": os.environ.get("SLACK_TOKEN"), 
    #         "channel": "task-list-test-channel",
    #         "text": f"Task {task.title} has been completed."
    #         })


    return make_response({'task': task.make_json()}, 200)

@task_bp.route("/<task_id>/mark_incomplete", methods=["PATCH"])

def mark_incomplete(task_id):
    task = Task.query.get(task_id)
    if not task:
        return make_response('',404)
    
    task.completed_at = None
    db.session.commit()

    return make_response({'task': task.make_json()}, 200)



