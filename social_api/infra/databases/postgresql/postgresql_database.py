from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from domain.entities.user_entity import UserEntity

from infra.databases.postgresql.config.database_connection import (
    DatabaseConnection,
)
from infra.databases.postgresql.models.user_base_model import UserBaseModel


class PostgreSQLDatabase:
    def __init__(self) -> None:
        self.database_connection = DatabaseConnection()
        self.session = None

    def __enter__(self):
        engine = self.database_connection.get_engine()
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

    def create_user(self, user: UserEntity) -> UserBaseModel:
        try:
            with PostgreSQLDatabase() as database:
                # TODO: add user attributes to UserBaseModel
                new_user = UserBaseModel()
                database.session.add()
                database.session.commit()
                return new_user
        except SQLAlchemyError:
            database.session.rollback()
