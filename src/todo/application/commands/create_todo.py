from dataclasses import dataclass

from src.todo.application.port.todo_repository import TodoRepository as ITodoRepository
from src.todo.domain import Todo


@dataclass
class CreateTodoCommand:
    """CreateTodoCommand is a command to create a new todo"""

    todo: Todo


class CreateTodoHandler:
    """CreateTodoHandler is the handler for CreateTodoCommand"""

    def __init__(self, repository: ITodoRepository):
        self.__repository = repository

    def handle(self, command: CreateTodoCommand) -> None:
        """Handle the CreateTodoCommand"""
        self.__repository.create_todo(command.todo)
