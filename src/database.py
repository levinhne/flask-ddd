from contextlib import contextmanager
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, scoped_session, sessionmaker


class Database:
    def __init__(self, db_url: str, echo: bool = False) -> None:
        """Khởi tạo Database với URL và engine."""
        self._engine = create_engine(db_url, echo=echo)
        self._session_factory = sessionmaker(
            autocommit=False, autoflush=False, bind=self._engine, expire_on_commit=False
        )
        self._scoped_session = scoped_session(self._session_factory)

    @contextmanager
    def session(self) -> Generator[Session, None, None]:
        """Context manager cho phiên làm việc với database."""
        db_session: Session = self._session_factory()
        try:
            yield db_session
        except Exception as e:
            db_session.rollback()  # Rollback khi có lỗi
            raise e
        finally:
            db_session.close()  # Đảm bảo đóng session

    def dispose(self) -> None:
        """Đóng engine khi không cần sử dụng nữa."""
        self._engine.dispose()
