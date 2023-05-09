from typing import List
from domain.entities.user_entity import UserEntity
import psycopg2

from infra.databases.postgresql.config.database_connection import (
    DatabaseConnection,
)
from infra.databases.postgresql.models.user_model import UserModel


class PostgreSQLDatabase:
    def __init__(self) -> None:
        self.database_connection = DatabaseConnection()
        self.cursor = None

    def __enter__(self):
        # TODO: create a cursor for interacting with the database
        self.cursor = None
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()

    def get_all_users(self) -> List[UserModel]:
        pass

    def create_user(self, user: UserEntity) -> UserModel:
        pass
