from typing import List
from domain.entities.comment_entity import CommentEntity
from domain.entities.post_entity import PostEntity
from domain.entities.user_entity import UserEntity
from data.models.comment_model import CommentModel
from data.models.post_model import PostModel
from data.models.user_model import UserModel
from domain.errors.exceptions import UserAlreadyExists
from domain.repositories.user_repository_interface import IUserRepository

# TODO: accessing something from the external layer
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

    def create_user(self, user: UserEntity) -> UserEntity:
        self.neo4j_database.create_user(user)
        user_base_model = self.postgresql_database.create_user(user)
        # return UserModel.from_user_base_model(user_base_model)

    def update_user(self, user: UserEntity) -> UserEntity:
        raise NotImplementedError()

    def delete_user(self, user: UserEntity) -> UserEntity:
        raise NotImplementedError()

    def get_user_by_username(self, username: str) -> UserEntity:
        raise NotImplementedError()

    def follow_user(self, first_username: str, second_username: str) -> None:
        raise NotImplementedError()

    def unfollow_user(self, first_username: str, second_username: str) -> None:
        raise NotImplementedError()

    def get_post_from_id(self, post_id: int) -> PostEntity:
        raise NotImplementedError()

    def get_all_user_followers(self, username: str) -> List[UserEntity]:
        raise NotImplementedError()

    def get_comments_from_post(self, post_id: int) -> List[CommentEntity]:
        raise NotImplementedError()
