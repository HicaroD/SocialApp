import os

from dotenv import load_dotenv
from neomodel import config
from datasources.errors.graph import UserNotFound, UserAlreadyExists
from datasources.models.user_node_model import UserNodeModel

load_dotenv(".environment")


class UserDatasource:
    def __init__(self) -> None:
        config.DATABASE_URL = os.getenv("NEO4J_BOLT_URL")

    def get_user(self, username: str) -> UserNodeModel | None:
        user = UserNodeModel.nodes.get_or_none(username=username)
        return user

    def get_all_users(self) -> list[str]:
        return [user.username for user in UserNodeModel.nodes.all()]

    def create_user(self, user_model: UserNodeModel) -> UserNodeModel:
        username = user_model.username

        user = self.get_user(username)
        if user is not None:
            raise UserAlreadyExists(f"User with username '{username}' already exists")

        user = UserNodeModel(username=username).save()
        return user

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

    # TODO(refactor): these methods below are too similar
    def follow_user(self, first_username: str, second_username) -> None:
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

    def unfollow_user(self, first_username: str, second_username) -> None:
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
