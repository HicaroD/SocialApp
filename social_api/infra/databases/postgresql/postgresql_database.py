from typing import List
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from domain.entities.user_entity import UserEntity

from infra.databases.postgresql.config.database_connection import (
    DatabaseConnection,
)
from infra.databases.postgresql.models.user_model import UserModel


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

    # TODO: I'm repetiting the same try-except, I need to refactor it
    def get_all_users(self) -> List[UserModel]:
        with PostgreSQLDatabase() as database:
            try:
                return database.session.query(UserModel).all()
            except SQLAlchemyError:
                database.session.rollback()

    def create_user(self, user: UserEntity) -> UserModel:
        with PostgreSQLDatabase() as database:
            try:
                # TODO: pretty sure there is a better way of doing it
                # without using all those fields
                new_user = UserModel(
                    name=user.name,
                    username=user.username,
                    email=user.email,
                    is_verified=user.email,
                )
                database.session.add(new_user)
                database.session.commit()
                return new_user
            except SQLAlchemyError:
                database.session.rollback()
