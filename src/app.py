from flask import Flask
from src.config import config
from src.internal.todo import register_blueprints as todo_register_blueprints
from src.extensions import register_extensions

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.url_map.strict_slashes = False 

    todo_register_blueprints(app)
    register_extensions(app)

    
    return app