from typing import List
from app.schemas.post import TextPost, VideoPost
from domain.entities.comment_entity import CommentEntity
from domain.entities.post_entity import PhotoPostEntity
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

    def post_text(self, username: str, post: TextPost) -> None:
        with DatabaseConnection() as database:
            # TODO: check if users exists
            query = f"""
            INSERT INTO socialapp_database.post (user_username_fk)
            VALUES ('{username}');

            INSERT INTO socialapp_database.textpost (post_id_fk, text)
            VALUES (LASTVAL(), '{post.text}');
            """
            database.execute_query(query)

    # TODO
    def post_video(self, username: str, post: VideoPost) -> None:
        with DatabaseConnection() as database:
            # TODO: check if users exists
            query = f"""
            INSERT INTO socialapp_database.post (user_username_fk)
            VALUES ('{username}');

            INSERT INTO socialapp_database.videopost (post_id_fk, video)
            VALUES (LASTVAL(), '{post.video}');
            """
            database.execute_query(query)

    def post_photo(self, username: str, post: PhotoPostEntity) -> None:
        with DatabaseConnection() as database:
            # TODO: check if users exists
            query = f"""
            INSERT INTO socialapp_database.post (user_username_fk)
            VALUES ('{username}');

            INSERT INTO socialapp_database.photopost (post_id_fk, photo)
            VALUES (LASTVAL(), '{post.photo}');
            """
            database.execute_query(query)

    def delete_post(self, post_id: int) -> None:
        with DatabaseConnection() as database:
            query = f"""
            DELETE FROM socialapp_database.post
            WHERE id = {post_id};
            """
            database.execute_query(query)

    def get_all_post_from_user(self, username: str) -> List:
        with DatabaseConnection() as database:
            query = f"""
            SELECT p.id
            FROM socialapp_database.post p
            WHERE p.user_username_fk = '{username}';
            """
            database.execute_query(query)
            posts = database.fetch_all_results()
            return posts

    def comment_in_post(self, username: str, post_id: int, comment: CommentEntity):
        with DatabaseConnection() as database:
            query = f"""
            INSERT INTO socialapp_database.comment (text)
            VALUES ('{comment.comment}');

            INSERT INTO socialapp_database.send (post_id_fk, comment_id_fk, user_username_fk)
            VALUES ({post_id}, LASTVAL(), '{username}');
            """
            database.execute_query(query)

    def get_all_comments_from_post(self, post_id) -> List:
        with DatabaseConnection() as database:
            query = f"""
            SELECT c.id, c.text
            FROM socialapp_database.send s
            JOIN socialapp_database.comment c ON s.comment_id_fk = c.id
            WHERE s.post_id_fk = {post_id};
            """
            database.execute_query(query)
            return database.fetch_all_results()

    def get_user_by_username(self, username: str) -> UserModel:
        with DatabaseConnection() as database:
            query = f"""
            SELECT *
            FROM socialapp_database.users users
            WHERE users.username = '{username}';
            """
            database.execute_query(query)
            return database.fetch_all_results()
