from flask import Flask

from src.extensions import db
from src.internal.todo.adapters.todo_repository import TodoRepository
from src.internal.todo.application.service import Service
from src.internal.todo.handlers.todo import create_todo_routers


def register_blueprints(app: Flask) -> None:
    app.register_blueprint(create_todo_routers(Service(TodoRepository(db.session))))
