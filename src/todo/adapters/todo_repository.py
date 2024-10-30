from sqlalchemy.orm import scoped_session

from src.todo.application.port.todo_repository import TodoRepository as ITodoRepository
from src.todo.domain.todo import NotFoundError, Todo


class TodoRepository(ITodoRepository):
    def __init__(self, session: scoped_session):
        self._session = session

    def create_todo(self, todo: Todo) -> None:
        with self._session() as session:
            try:
                session.add(todo)
                session.commit()
            except Exception as e:
                raise RuntimeError(f"Database error: {e}")

    def list_todos(self) -> list[Todo]:
        with self._session() as session:
            try:
                todos = session.query(Todo).all()
            except Exception as e:
                raise RuntimeError(f"Database error: {e}")

            return todos

    def get_todo_by_id(self, id: int) -> Todo:
        with self._session() as session:
            try:
                todo = session.query(Todo).get(id)
                if not todo:
                    raise NotFoundError(f"Todo with id {id} not found")
                return todo
            except Exception as e:
                raise RuntimeError(f"Database error: {e}")
