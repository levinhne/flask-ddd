from src.internal.todo.application.port.todo_repository import (
    TodoRepository as ITodoRepository,
)
from src.internal.todo.application.queries.query import Query
from src.internal.todo.domain.todo import Todo


class ListTodos(Query):
    def is_query():
        pass


class ListTodosHandler:
    def __init__(self, repository: ITodoRepository):
        self.__repository = repository

    def handle(self, query: Query) -> list[Todo]:
        if isinstance(query, ListTodos):
            return self.__repository.list_todos()
        else:
            raise Exception("Query is not a ListTodos instance")
