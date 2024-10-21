from sqlalchemy.orm import Session
from src.application.port.todo_repository import TodoRepository as ITodoRepository
from src.domain.todo import Todo

class TodoRepository(ITodoRepository):
    def __init__(self, session: Session):
        self.__session = session

    def list_todos(self) -> list[Todo]:
        try:
            todos = self.__session.query(Todo).all()
        except Exception as e:
            raise e
        finally:
            self.__session.close()
        return todos

    def get_todo_by_id(self, id: int) -> Todo:
        try:
            todo = self.__session.query(Todo).get(id)
        except Exception as e:
            raise e # Handle the exception
        finally:
            self.__session.close()
        return todo