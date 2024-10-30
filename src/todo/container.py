
from dependency_injector import containers, providers

from src.config import Config
from src.database import Database
from src.todo.adapters.todo_repository import TodoRepository
from src.todo.application.service import Service


class Container(containers.DeclarativeContainer):
    config = providers.Object(Config)
    
    db = providers.Singleton(Database, db_url=config.provided.DATABASE_URL)
    repository = providers.Factory(TodoRepository, session=db.provided.session)
    service = providers.Factory(Service, repository=repository)
