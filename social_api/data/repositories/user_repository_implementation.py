from typing import List
from app.schemas.post import PhotoPost, TextPostEntity, VideoPostEntity
from domain.entities.comment_entity import CommentEntity
from domain.entities.post_entity import PhotoPostEntity, PostEntity
from domain.entities.user_entity import UserEntity

from infra.databases.neo4j.neo4j_database import Neo4JDatabase
from infra.databases.postgresql.postgresql_database import PostgreSQLDatabase


class UserRepository:
    def __init__(
        self,
        postgresql_database: PostgreSQLDatabase,
        neo4j_database: Neo4JDatabase,
    ) -> None:
        self.postgresql_database = postgresql_database
        self.neo4j_database = neo4j_database

    def get_all_users(self) -> List[UserEntity]:
        return self.postgresql_database.get_all_users()

    def create_user(self, user: UserEntity):
        self.postgresql_database.create_user(user)
        self.neo4j_database.create_user(user)

    def update_user(self, username: str, user: UserEntity):
        self.neo4j_database.update_user(username, user)
        self.postgresql_database.update_user(username, user)

    def delete_user(self, username: str):
        self.neo4j_database.delete_user(username)
        self.postgresql_database.delete_user(username)

    def get_user_by_username(self, username: str) -> UserEntity:
        raise NotImplementedError()

    def follow_user(self, first_username: str, second_username: str) -> None:
        self.neo4j_database.follow_user(first_username, second_username)

    def unfollow_user(self, first_username: str, second_username: str) -> None:
        self.neo4j_database.unfollow_user(first_username, second_username)

    # TODO
    def post_photo(self, username: str, photo_post: PhotoPostEntity) -> None:
        # Check if user exists before post
        self.postgresql_database.post_photo(username, photo_post)
        raise NotImplementedError()

    def post_video(self, username: str, photo_post: VideoPostEntity) -> None:
        # Check if user exists before post
        self.postgresql_database.post_photo(username, photo_post)
        raise NotImplementedError()

    def post_text(self, username: str, photo_post: TextPostEntity) -> None:
        # Check if user exists before post
        self.postgresql_database.post_photo(username, photo_post)
        raise NotImplementedError()

    # TODO
    def get_all_user_comments_from_post(self, username: str, post_id: str) -> List:
        raise NotImplementedError()

    # TODO
    def get_all_posts_from_user(self, username: str) -> List:
        raise NotImplementedError()

    # TODO
    def get_post_from_id(self, post_id: int) -> PostEntity:
        raise NotImplementedError()

    # TODO
    def get_comments_from_post(self, post_id: int) -> List[CommentEntity]:
        raise NotImplementedError()

    # TODO
    def delete_post(self, post_id: str) -> None:
        raise NotImplementedError()

    # TODO
    def comment_in_post(self, post_id: str, comment: CommentEntity) -> None:
        raise NotImplementedError()

    def get_all_following_users(self, username: str) -> List[UserEntity]:
        following_user_usernames = self.neo4j_database.get_all_following_users(username)
        # TODO: Get each user in PostgreSQL database
        return following_user_usernames

    def get_all_user_followers(self, username: str) -> List[UserEntity]:
        followers = self.neo4j_database.get_all_user_followers(username)
        # TODO: Get each user in PostgreSQL database
        return followers
