from dataclasses import dataclass

from src.todo.application.port.todo_repository import TodoRepository as ITodoRepository
from src.todo.application.queries.query import Query
from src.todo.domain import Todo


@dataclass
class GetTodoByID(Query):
    id: int

    def is_query(self):
        pass


class GetTodoByTitle(Query):
    def __init__(self, title: str):
        self.title = title

    def is_query(self):
        pass


class GetTodoHandler:
    def __init__(self, repository: ITodoRepository):
        self.__repository = repository

    def handle(self, query: Query) -> Todo:
        if isinstance(query, GetTodoByID):
            return self.__repository.get_todo_by_id(query.id)
        else:
            raise Exception("Query not found")
