from typing import List
from app.schemas.post import TextPostEntity, VideoPostEntity
from domain.entities.post_entity import PhotoPostEntity, PostEntity
from domain.entities.user_entity import UserEntity
from domain.errors.exceptions import UserAlreadyExists

from infra.databases.postgresql.config.database_connection import (
    DatabaseConnection,
)

from infra.databases.postgresql.models.user_model import UserModel
from psycopg2.errors import UniqueViolation


class PostgreSQLDatabase:
    def __init__(self) -> None:
        pass

    def get_all_users(self) -> List[UserModel]:
        with DatabaseConnection() as database:
            database.execute_query("SELECT * FROM socialapp_database.users")
            users = database.fetch_all_results()
            return users

    def create_user(self, user: UserEntity) -> UserModel:
        try:
            with DatabaseConnection() as database:
                is_verified = "true" if user.is_verified else "false"
                query = f"""
                INSERT INTO socialapp_database.users
                ("name", username, email, is_verified)
                VALUES('{user.name}', '{user.username}', '{user.email}', {is_verified});
                """
                database.execute_query(query)
        except UniqueViolation:
            raise UserAlreadyExists(
                f"User with username '{user.username} already exists'"
            )

    def update_user(self, username: str, user: UserEntity) -> None:
        with DatabaseConnection() as database:
            is_verified = "true" if user.is_verified else "false"
            query = f"""
            UPDATE socialapp_database.users
            SET "name" = '{user.name}', username = '{user.username}', email = '{user.email}', is_verified = {is_verified}
            WHERE username = '{username}';
            """
            database.execute_query(query)

    def delete_user(self, username: str) -> None:
        with DatabaseConnection() as database:
            query = f"""
            DELETE FROM socialapp_database.users WHERE username = '{username}'
            """
            database.execute_query(query)

    # TODO
    def post_photo(self, username: str, post: PhotoPostEntity) -> None:
        raise NotImplementedError()

    # TODO
    def post_video(self, username: str, post: VideoPostEntity) -> None:
        raise NotImplementedError()

    # TODO
    def post_text(self, username: str, post: TextPostEntity) -> None:
        raise NotImplementedError()
