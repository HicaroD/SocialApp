import os

from dotenv import load_dotenv
from neomodel import config

from domain.errors.exceptions import UserAlreadyExists, UserNotFound
from infra.databases.neo4j.models.user_node_model import UserNodeModel
from domain.entities.user_entity import UserEntity

load_dotenv(".environment")


class Neo4JDatabase:
    def __init__(self) -> None:
        config.DATABASE_URL = os.getenv("NEO4J_BOLT_URL")

    def get_user(self, username: str) -> UserNodeModel | None:
        return UserNodeModel.nodes.get_or_none(username=username)

    def get_all_users(self) -> list[str]:
        return [user.username for user in UserNodeModel.nodes.all()]

    def create_user(self, user_entity: UserEntity) -> None:
        user = self.get_user(user_entity.username)
        if user is not None:
            raise UserAlreadyExists(
                f"User with username '{user_entity.username}' already exists"
            )
        UserNodeModel(username=user_entity.username).save()

    def update_user(self, old_username: str, new_username: str) -> UserNodeModel:
        user = self.get_user(old_username)
        if user is None:
            raise UserNotFound(f"User with username '{old_username}' does not exists")
        user.create_or_update()

    def delete_user(self, username: str) -> None:
        user = self.get_user(username)
        if user is None:
            raise UserNotFound(f"User with username '{username}' does not exists")
        user.delete()

    def get_all_following_users(self, username: str) -> list[str]:
        user = self.get_user(username)
        if user is None:
            raise UserNotFound(f"User with username '{username}' does not exists.")
        following_users_of_user = user.get_all_following_users()
        return following_users_of_user

    def get_all_user_followers(self, username: str) -> list[str]:
        user = self.get_user(username)
        if user is None:
            raise UserNotFound(f"User with username '{username}' does not exists.")
        user_followers = user.get_all_followers()
        return user_followers

    # TODO: avoid code repetition
    def follow_user(
        self,
        first_username: str,
        second_username: str,
    ) -> None:
        first_user = self.get_user(first_username)
        second_user = self.get_user(second_username)

        if first_user is None:
            raise UserNotFound(
                f"User with username '{first_username}' does not exists."
            )

        if second_user is None:
            raise UserNotFound(
                f"User with username '{second_username}' does not exists."
            )

        first_user.follows.connect(second_user)

    def unfollow_user(
        self,
        first_username: str,
        second_username: str,
    ) -> None:
        first_user = self.get_user(first_username)
        second_user = self.get_user(second_username)

        if first_user is None:
            raise UserNotFound(
                f"User with username '{first_username}' does not exists."
            )

        if second_user is None:
            raise UserNotFound(
                f"User with username '{second_username}' does not exists."
            )
        first_user.follows.disconnect(second_user)
