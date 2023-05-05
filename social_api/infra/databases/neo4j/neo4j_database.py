import os

from dotenv import load_dotenv
from neomodel import config

from domain.errors.exceptions import UserAlreadyExists, UserNotFound
from infra.databases.neo4j.models.user_node_model import UserNodeModel
from domain.entities.user import User

load_dotenv(".environment")


class Neo4JDatabase:
    def __init__(self) -> None:
        config.DATABASE_URL = os.getenv("NEO4J_BOLT_URL")

    def get_user(self, user: User) -> UserNodeModel | None:
        return UserNodeModel.nodes.get_or_none(username=user.username)

    def get_all_users(self) -> list[str]:
        return [user.username for user in UserNodeModel.nodes.all()]

    def create_user(self, user_entity: User) -> UserNodeModel:
        user = self.get_user(user_entity)
        if user is not None:
            raise UserAlreadyExists(
                f"User with username '{user_entity.username}' already exists"
            )

        user = UserNodeModel(username=user_entity.username).save()
        return user

    def get_all_following_users(self, user_entity: User) -> list[str]:
        user = self.get_user(user_entity)
        if user is None:
            raise UserNotFound(
                f"User with username '{user_entity.username}' does not exists."
            )
        following_users_of_user = user.get_all_following_users()
        return following_users_of_user

    def get_all_user_followers(self, user_entity: User) -> list[str]:
        user = self.get_user(user_entity)
        if user is None:
            raise UserNotFound(
                f"User with username '{user_entity.username}' does not exists."
            )
        user_followers = user.get_all_followers()
        return user_followers

    # TODO: avoid code repetition
    def follow_user(
        self,
        first_user_entity: User,
        second_user_entity: User,
    ) -> None:
        first_user = self.get_user(first_user_entity)
        second_user = self.get_user(second_user_entity)

        if first_user is None:
            raise UserNotFound(
                f"User with username '{first_user_entity.username}' does not exists."
            )

        if second_user is None:
            raise UserNotFound(
                f"User with username '{second_user_entity.username}' does not exists."
            )

        first_user.follows.connect(second_user)

    def unfollow_user(
        self,
        first_user_entity: User,
        second_user_entity: User,
    ) -> None:
        first_user = self.get_user(first_user_entity)
        second_user = self.get_user(second_user_entity)

        if first_user is None:
            raise UserNotFound(
                f"User with username '{first_user_entity.username}' does not exists."
            )

        if second_user is None:
            raise UserNotFound(
                f"User with username '{second_user_entity.username}' does not exists."
            )
        first_user.follows.disconnect(second_user)
