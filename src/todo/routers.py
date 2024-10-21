from flask import Blueprint, request, jsonify, current_app
from pydantic import BaseModel

class TodoRequest(BaseModel):
    title: str
    description: str

todo_blueprint = Blueprint("todo", __name__, url_prefix="/todos")

@todo_blueprint.route("/", methods=["GET"])
def list_todos():
    req = TodoRequest(**request.args.to_dict())
    current_app.logger.info(f"List todos with title: {req.title}")
    return jsonify({}), 200
    
