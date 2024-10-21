from src.application.queries.query import Query
from src.domain.todo import Todo 
from src.application.port.todo_repository import TodoRepository as ITodoRepository

class GetTodoByID(Query):
    def __init__(self, id: int):
        self.id = id
    
    def is_query():
        pass
    
class GetTodoByTitle(Query):
    def __init__(self, title: str):
        self.title = title
    
    def is_query():
        pass
    
class GetTodoHandler():
    def __init__(self, repository: ITodoRepository):
        self.__repository = repository
    
    def handle(self, query: Query) -> Todo:
        if isinstance(query, GetTodoByID):
            return self.__repository.get_todo_by_id(query.id)
        elif isinstance(query, GetTodoByTitle):
            return self.__repository.get_todo_by_title(query.title)
        else:
            raise Exception("Query not found")