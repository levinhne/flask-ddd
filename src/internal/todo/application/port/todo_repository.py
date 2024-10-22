from abc import ABC, abstractmethod
from src.internal.todo.domain.todo import Todo

class TodoRepository(ABC):
    @abstractmethod
    def create_todo(self, todo: Todo) -> Todo:
        pass
    
    @abstractmethod
    def list_todos(self) -> list[Todo]:
        pass

    @abstractmethod
    def get_todo_by_id(self, id:int) -> Todo:
        pass
    