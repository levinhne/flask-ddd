from dependency_injector import containers, providers

from src.extensions import db
from src.todo.adapters.todo_repository import TodoRepository
from src.todo.application.service import Service


class Container(containers.DeclarativeContainer):
    session = providers.Singleton(lambda: db.session)
    repository = providers.Factory(TodoRepository, session=session.provided.session)
    service = providers.Factory(Service, repository=repository)
