from sqlalchemy.orm import sessionmaker

from infra.databases.postgresql.config.database_connection import (
    DatabaseConnection,
)


class PostgreSQLDatabase:
    def __init__(self) -> None:
        self.database_connection = DatabaseConnection()

    def __enter__(self):
        engine = self.database_connection.get_engine()
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
