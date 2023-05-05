from typing import List
from domain.entities.comment import Comment
from domain.entities.post import Post
from domain.entities.user import User
from domain.repositories.user_repository_interface import IUserRepository
from infra.databases.neo4j.neo4j_database import Neo4JDatabase
from infra.databases.postgresql.postgresql_database import PostgreSQLDatabase


class UserRepository(IUserRepository):
    def __init__(
        self,
        postgresql_database: PostgreSQLDatabase,
        neo4j_database: Neo4JDatabase,
    ) -> None:
        self.postgresql_database = postgresql_database
        self.neo4j_database = neo4j_database

    def create_user(self, user: User) -> User:
        raise NotImplementedError()

    def update_user(self, user: User) -> User:
        raise NotImplementedError()

    def delete_user(self, user: User) -> User:
        raise NotImplementedError()

    def get_user_by_username(self, username: str) -> User:
        raise NotImplementedError()

    def follow_user(self, first_username: str, second_username: str) -> None:
        raise NotImplementedError()

    def unfollow_user(self, first_username: str, second_username: str) -> None:
        raise NotImplementedError()

    def get_post_from_id(self, post_id: int) -> Post:
        raise NotImplementedError()

    def get_all_user_followers(self, username: str) -> List[User]:
        raise NotImplementedError()

    def get_comments_from_post(self, post_id: int) -> List[Comment]:
        raise NotImplementedError()
