from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class NotFoundError(Exception):
    pass

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

    def to_dict(self):
        """Return a dictionary representation of the Todo object."""
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    def from_dict(self, data):
        """Create a Todo object from a dictionary."""
        return Todo(
            title=data.get("title"),
            completed=data.get("completed"),
        )
