from src.internal.todo.domain.todo import Todo
from src.internal.todo.application.port.todo_repository import TodoRepository as ITodoRepository


class CreateTodoCommand():
    def __init__(self, todo: Todo):
        self.todo = todo
    

class CreateTodoHandler:
    def __init__(self, repository: ITodoRepository):
        self.__repository = repository

    def handle(self, command: CreateTodoCommand) -> None:
        self.__repository.create_todo(command.todo)
