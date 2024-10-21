from abc import ABC, abstractmethod
from src.domain.todo import Todo
from src.application.queries.query import Query
from src.application.queries.get_todo import GetTodoHandler
from src.application.port.todo_repository import TodoRepository as ITodoRepository

class ServiceApplication(ABC):
    @abstractmethod
    def get_todo_by_id(self, id:int) -> dict:
        pass


class Queries():
    def __init__(self, repository: ITodoRepository) -> None:
        self.get_todo_handler = GetTodoHandler(repository)

class Service(ServiceApplication):
    def __init__(self, repository: ITodoRepository) -> None:
        self.quries = Queries(repository)

    def get_todo_by_id(self, query: Query) -> Todo:
        return self.quries.get_todo_handler.handle(query)
