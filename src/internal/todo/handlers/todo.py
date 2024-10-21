from flask import Blueprint, jsonify
from src.internal.todo.application.service import ServiceApplication
from src.internal.todo.application.queries.get_todo import GetTodoByID

bp = Blueprint('todo', __name__, url_prefix='/todos')

def create_todo_routers(app: ServiceApplication):
    @bp.route('/<int:id>', methods=['GET'])
    def get_by_id(id):
        todo = app.get_todo_by_id(GetTodoByID(id))
        return jsonify(todo.to_dict())

    return bp
