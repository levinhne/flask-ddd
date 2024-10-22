from flask import Blueprint, abort, jsonify, request

from src.internal.todo.application.queries.get_todo import GetTodoByID
from src.internal.todo.application.queries.list_todos import ListTodos
from src.internal.todo.application.service import ServiceApplication
from src.internal.todo.domain.todo import NotFoundError
from src.internal.todo.application.commands.create_todo import CreateTodoCommand
from src.internal.todo.domain.todo import Todo
from src.extensions import db

bp = Blueprint("todo", __name__, url_prefix="/todos")

@bp.before_app_request
def init_db():
    db.create_all()

def create_todo_routers(app: ServiceApplication):

    @bp.route("/", methods=["POST"])
    def create_todo():
        try:
            todo = Todo()
            todo.title = request.json["title"]
            result = app.create_todo(CreateTodoCommand(
                todo
            ))
            return jsonify(todo.to_dict()), 201
        except Exception as e:
            abort(500, description=str(e))

    @bp.route("/", methods=["GET"])
    def list_todos():
        try:
            todos = app.list_todos(ListTodos())
            return jsonify([todo.to_dict() for todo in todos])
        except Exception as e:
            abort(500, description=str(e))

    @bp.route("/<int:id>", methods=["GET"])
    def get_by_id(id):
        try:
            todo = app.get_todo_by_id(GetTodoByID(id))
            if not todo:
                abort(404, "Todo not found")
            return jsonify(todo.to_dict())
        except NotFoundError as e:
            abort(404, description=str(e))
        except Exception as e:
            abort(500, description=str(e))

    return bp
