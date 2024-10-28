from flask import Flask

import src.todo.handlers.todo as todo
from src.todo.container import Container

def register_blueprints(app: Flask) -> None:
    container = Container()
    container.init_resources()
    container.wire(modules=[todo.__name__])
    app.register_blueprint(todo.bp)

