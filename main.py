from flask import Flask
from flask import request
from CRUD_USERS import create_user, read_user, update_user, delete_user
from CRUD_PROJECTS import create_project, read_project, update_project, delete_project
from CRUD_TASKS import create_task, read_task, update_task, delete_task
from api_users import list_of_active_users, select_user
from api_projects import select_project, list_of_active_projects
from api_tasks import select_task, list_of_active_tasks
from kanban_table_select import select_kanban
import json

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/about")
def about():
    return "About"


@app.route("/test")
def test():
    test_results: str = ""
    try:
        r = list_of_active_users()
        dump = json.dumps(r)
        print(dump)
        test_results += "Test of list_of_active_users was successful.</br>"
    except Exception as e:
        test_results += "Test of list_of_active_users was unsuccessful. " + e.__str__() + "</br>"
    try:
        r = list_of_active_tasks()
        dump = json.dumps(r)
        print(dump)
        test_results += "Test of list_of_active_tasks was successful.</br>"
    except Exception as e:
        test_results += "Test of list_of_active_tasks was unsuccessful." + e.__str__() + "</br>"

    return test_results


@app.route("/api", methods=["GET"])
def hello_api():
    return "Hello API!"


@app.route("/api/kanban", methods=["GET"])
def kanban_select():
    try:
        project_id: int = int(request.args.get("project_id", ""))
        r = json.dumps(select_kanban(project_id))
        return r
    except Exception as e:
        return {"r": 0,
                "error_code": -9,
                "error_description": e.__str__()}


# Работа с пользователями
# ///////////////////////

@app.route("/api/users", methods=["GET"])
def api_users():
    try:
        name: str = str(request.args.get("name", ""))
        print(type(name))
        print("///////////" + name)
        r = json.dumps(select_user(name))
        return r
    except Exception as e:
        return {"r": 0,
                "error_code": -9,
                "error_description": e.__str__()}


@app.route("/api/users/list", methods=["GET"])
def api_users_list():
    try:
        r = list_of_active_users()
        dump = json.dumps(r)
        return dump
    except Exception as e:
        return {"r": 0,
                "error_code": -9,
                "error_description": e.__str__()}


@app.route("/api/users/add", methods=["GET"])
def api_users_add():
    try:
        name: str = str(request.args.get("name", ""))
        r = json.dumps(create_user(name))
        return r
    except Exception as e:
        return {"r": 0,
                "error_code": -9,
                "error_description": e.__str__()}


@app.route("/api/users/read", methods=["GET"])
def api_users_read():
    try:
        value: int = int(request.args.get("value", ""))
        r = json.dumps(read_user(value))
        return r
    except Exception as e:
        return {"r": 0,
                "error_code": -9,
                "error_description": e.__str__()}


@app.route("/api/users/update", methods=["GET"])
def api_users_update():
    try:
        value: int = int(request.args.get("value", ""))
        name: str = str(request.args.get("name", ""))
        r = json.dumps(update_user(value, name))
        return r
    except Exception as e:
        return {"r": 0,
                "error_code": -9,
                "error_description": e.__str__()}


@app.route("/api/users/delete", methods=["GET"])
def api_users_delete():
    try:
        value: int = int(request.args.get("value", ""))
        r = json.dumps(delete_user(value))
        return r
    except Exception as e:
        return {"r": 0,
                "error_code": -9,
                "error_description": e.__str__()}


# Работа с проектами
# //////////////////

@app.route("/api/projects", methods=["GET"])
def api_projects():
    try:
        name: str = str(request.args.get("name", ""))
        r = json.dumps(select_project(name))
        return r
    except Exception as e:
        return {"r": 0,
                "error_code": -9,
                "error_description": e.__str__()}


@app.route("/api/projects/list", methods=["GET"])
def api_projects_list():
    try:
        r = list_of_active_projects()
        dump = json.dumps(r)
        return dump
    except Exception as e:
        return {"r": 0,
                "error_code": -9,
                "error_description": e.__str__()}


@app.route("/api/projects/add", methods=["GET"])
def api_projects_add():
    try:
        name: str = str(request.args.get("name", ""))
        r = json.dumps(create_project(name))
        return r
    except Exception as e:
        return {"r": 0,
                "error_code": -9,
                "error_description": e.__str__()}


@app.route("/api/projects/read", methods=["GET"])
def api_projects_read():
    try:
        value: int = int(request.args.get("value", ""))
        r = json.dumps(read_project(value))
        return r
    except Exception as e:
        return {"r": 0,
                "error_code": -9,
                "error_description": e.__str__()}


@app.route("/api/projects/update", methods=["GET"])
def api_projects_update():
    try:
        value: int = int(request.args.get("value", ""))
        name: str = str(request.args.get("name", ""))
        r = json.dumps(update_project(value, name))
        return r
    except Exception as e:
        return {"r": 0,
                "error_code": -9,
                "error_description": e.__str__()}


@app.route("/api/projects/delete", methods=["GET"])
def api_projects_delete():
    try:
        value: int = int(request.args.get("value", ""))
        r = json.dumps(delete_project(value))
        return r
    except Exception as e:
        return {"r": 0,
                "error_code": -9,
                "error_description": e.__str__()}


# Работа с задачами
# /////////////////

@app.route("/api/tasks", methods=["GET"])
def api_tasks():
    try:
        name: str = str(request.args.get("name", ""))
        r = json.dumps(select_task(name))
        return r
    except Exception as e:
        return {"r": 0,
                "error_code": -9,
                "error_description": e.__str__()}


@app.route("/api/tasks/list", methods=["GET"])
def api_tasks_list():
    try:
        r = list_of_active_tasks()
        dump = json.dumps(r)
        return dump
    except Exception as e:
        return {"r": 0,
                "error_code": -9,
                "error_description": e.__str__()}


@app.route("/api/tasks/add", methods=["GET"])
def api_tasks_add():
    try:
        name: str = str(request.args.get("name", ""))
        task_id: int = int(request.args.get("project_id", ""))
        user_id: int = int(request.args.get("user_id", ""))
        r = json.dumps(create_task(name, task_id, user_id))
        return r
    except Exception as e:
        return {"r": 0,
                "error_code": -9,
                "error_description": e.__str__()}


@app.route("/api/tasks/read", methods=["GET"])
def api_tasks_read():
    try:
        value: int = int(request.args.get("value", ""))
        r = json.dumps(read_task(value))
        return r
    except Exception as e:
        return {"r": 0,
                "error_code": -9,
                "error_description": e.__str__()}


@app.route("/api/tasks/update", methods=["GET"])
def api_tasks_update():
    try:
        value: int = int(request.args.get("value", ""))
        name: str = str(request.args.get("name", ""))
        r = json.dumps(update_task(value, name))
        return r
    except Exception as e:
        return {"r": 0,
                "error_code": -9,
                "error_description": e.__str__()}


@app.route("/api/tasks/delete", methods=["GET"])
def api_tasks_delete():
    try:
        value: int = int(request.args.get("value", ""))
        r = json.dumps(delete_task(value))
        return r
    except Exception as e:
        return {"r": 0,
                "error_code": -9,
                "error_description": e.__str__()}


if __name__ == "__main__":
    # print(list_of_active_users())
    # print("lllllllllll")
    # print(api_users_list())
    app.run(host='0.0.0.0', port=5000)

