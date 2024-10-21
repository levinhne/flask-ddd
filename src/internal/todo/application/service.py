from abc import ABC, abstractmethod

from src.internal.todo.application.port.todo_repository import (
    TodoRepository as ITodoRepository,
)
from src.internal.todo.application.queries.get_todo import GetTodoHandler
from src.internal.todo.application.queries.list_todos import ListTodosHandler
from src.internal.todo.application.queries.query import Query
from src.internal.todo.domain.todo import Todo


class ServiceApplication(ABC):
    @abstractmethod
    def list_todos(self, query: Query) -> list[Todo]:
        pass

    @abstractmethod
    def get_todo_by_id(self, query: Query) -> Todo:
        pass

class Queries:
    def __init__(self, repository: ITodoRepository) -> None:
        self.get_todo_handler = GetTodoHandler(repository)
        self.list_todos_handler = ListTodosHandler(repository)


class Service(ServiceApplication):
    def __init__(self, repository: ITodoRepository) -> None:
        self.quries = Queries(repository)

    def list_todos(self, query: Query) -> list[Todo]:
        return self.quries.list_todos_handler.handle(query)

    def get_todo_by_id(self, query: Query) -> Todo:
        return self.quries.get_todo_handler.handle(query)
