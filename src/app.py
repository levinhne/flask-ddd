from flask import Flask

from src.config import config
from src.todo import register_blueprints as todo_register_blueprints


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.url_map.strict_slashes = False

    todo_register_blueprints(app)

    return app

