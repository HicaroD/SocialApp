from typing import List
from domain.entities.user_entity import UserEntity

from infra.databases.postgresql.config.database_connection import (
    DatabaseConnection,
)

from infra.databases.postgresql.models.user_model import UserModel


class PostgreSQLDatabase:
    def __init__(self) -> None:
        pass

    def get_all_users(self) -> List[UserModel]:
        with DatabaseConnection() as database:
            database.execute_query("SELECT * FROM socialapp_database.users")
            users = database.fetch_all_results()
            return users

    def create_user(self, user: UserEntity) -> UserModel:
        # TODO: line is too big
        with DatabaseConnection() as database:
            is_verified = "true" if user.is_verified else "false"
            query = f"""
            INSERT INTO socialapp_database.users
            ("name", username, email, is_verified)
            VALUES('{user.name}', '{user.username}', '{user.email}', {is_verified});
            """
            database.execute_query(query)
