from abc import ABC, abstractmethod

from src.todo.application.commands.create_todo import (
    CreateTodoCommand,
    CreateTodoHandler,
)
from src.todo.application.port.todo_repository import TodoRepository as ITodoRepository
from src.todo.application.queries.get_todo import GetTodoHandler
from src.todo.application.queries.list_todos import ListTodosHandler
from src.todo.application.queries.query import Query
from src.todo.domain.todo import Todo


class ServiceApplication(ABC):

    @abstractmethod
    def create_todo(self, command: CreateTodoCommand) -> None:
        pass

    @abstractmethod
    def list_todos(self, query: Query) -> list[Todo]:
        pass

    @abstractmethod
    def get_todo_by_id(self, query: Query) -> Todo:
        pass


class Commands:
    def __init__(self, repository: ITodoRepository) -> None:
        self.create_todo_handler = CreateTodoHandler(repository)


class Queries:
    def __init__(self, repository: ITodoRepository) -> None:
        self.get_todo_handler = GetTodoHandler(repository)
        self.list_todos_handler = ListTodosHandler(repository)


class Service(ServiceApplication):
    def __init__(self, repository: ITodoRepository) -> None:
        self.quries = Queries(repository)
        self.commands = Commands(repository)

    def create_todo(self, command: CreateTodoCommand) -> None:
        return self.commands.create_todo_handler.handle(command)

    def list_todos(self, query: Query) -> list[Todo]:
        return self.quries.list_todos_handler.handle(query)

    def get_todo_by_id(self, query: Query) -> Todo:
        return self.quries.get_todo_handler.handle(query)
