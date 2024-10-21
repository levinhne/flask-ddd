from flask import Blueprint, jsonify, abort
from src.internal.todo.application.service import ServiceApplication
from src.internal.todo.application.queries.get_todo import GetTodoByID

bp = Blueprint('todo', __name__, url_prefix='/todos')

def create_todo_routers(app: ServiceApplication):
    @bp.route('/<int:id>', methods=['GET'])
    def get_by_id(id):
        try: 
            todo = app.get_todo_by_id(GetTodoByID(id))
            if not todo:
                abort(404, 'Todo not found')
            return jsonify(todo.to_dict())
        except Exception as e:
            abort(500, description=str(e))

    return bp
