from dataclasses import dataclass

from src.todo.application.port.todo_repository import TodoRepository as ITodoRepository
from src.todo.application.queries.query import Query
from src.todo.domain import Todo


@dataclass
class ListTodos(Query):

    def is_query(self):
        pass


class ListTodosHandler:
    def __init__(self, repository: ITodoRepository):
        self.__repository = repository

    def handle(self, query: Query) -> list[Todo]:
        if isinstance(query, ListTodos):
            return self.__repository.list_todos()
        else:
            raise Exception("Query is not a ListTodos instance")
