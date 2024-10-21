from sqlalchemy.orm import scoped_session
from src.internal.todo.application.port.todo_repository import TodoRepository as ITodoRepository
from src.internal.todo.domain.todo import Todo
from src.internal.todo.domain.todo import NotFoundError

class TodoRepository(ITodoRepository):
    def __init__(self, session: scoped_session):
        self.__session = session

    def list_todos(self) -> list[Todo]:
        try:
            todos = self.__session.query(Todo).all()
        except Exception as e:
            raise RuntimeError(f"Database error: {e}")
        finally:
            self.__session.close()
        return todos

    def get_todo_by_id(self, id: int) -> Todo:
        try:
            todo = self.__session.query(Todo).get(id)
            if not todo:
                raise NotFoundError(f"Todo with id {id} not found")
            return todo
        except Exception as e:
            raise RuntimeError(f"Database error: {e}")
        finally:
            self.__session.close()

