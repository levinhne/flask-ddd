from http import HTTPStatus

from dependency_injector.wiring import Provide, inject
from flask import Blueprint, abort, jsonify, request

from src.todo.application.commands.create_todo import CreateTodoCommand
from src.todo.application.queries.get_todo import GetTodoByID
from src.todo.application.queries.list_todos import ListTodos
from src.todo.application.service import Service, ServiceApplication
from src.todo.container import Container
from src.todo.domain.todo import NotFoundError, Todo

bp = Blueprint("todo", __name__, url_prefix="/todos")


@bp.route("/", methods=["POST"])
@inject
def create_todo(app: ServiceApplication = Provide[Container.service]):
    """Create a new todo"""
    try:
        todo = Todo(title="dfdfdf")
        app.create_todo(CreateTodoCommand(todo=todo))
        return jsonify(todo.to_dict()), HTTPStatus.CREATED
    except ValueError as e:
        abort(400, description=str(e))
    except TypeError as e:
        abort(400, description=str(e))


@bp.route("/", methods=["GET"])
@inject
def list_todos(app: ServiceApplication = Provide[Container.service]):
    """List all todos"""
    try:
        todos = app.list_todos(ListTodos())
        return jsonify([todo.to_dict() for todo in todos])
    except Exception as e:
        abort(500, description=str(e))


@bp.route("/<int:id>", methods=["GET"])
@inject
def get_by_id(id, app: ServiceApplication = Provide[Container.service]):
    """Get a todo by id"""
    try:
        todo = app.get_todo_by_id(GetTodoByID(id=id))
        if not todo:
            abort(404, "Todo not found")
        return jsonify(todo.to_dict())
    except NotFoundError as e:
        abort(404, description=str(e))
    except Exception as e:
        abort(500, description=str(e))
