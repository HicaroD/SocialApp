# TODO(REFACTOR): lines are too big!
# I'll be using a OGM for Neo4J in order to simplify all queries


# class CypherCommands:
#     @staticmethod
#     def get_all_users_command():
#         return "MATCH (user: User) RETURN user"

#     @staticmethod
#     def get_create_user_command(user: UserModel):
#         name = user.name
#         username = user.username
#         age = user.age
#         description = "" if user.description is None else user.description
#         profile_picture = "" if user.profile_picture is None else user.profile_picture

#         return f"""MERGE (user: User {{username: "{username}", name: "{name}", "age: "{age}", description: "{description}", profile_picture: "{profile_picture}"}})"""

#     @staticmethod
#     def get_all_following_users(username: str):
#         return f"""MATCH (u:User {{name: "{username}"}})-[:FOLLOWS]->(following)
#         RETURN following"""

#     @staticmethod
#     def get_all_users_followers_command(username: str):
#         return f"""MATCH (u:User {{name: "{username}"}})<-[:FOLLOWS]-(follower)
#         RETURN follower"""

#     @staticmethod
#     def follow_user_command(first_username: str, second_username: str):
#         return f"""MATCH (u1:User {{name: "{first_username}"}}), (u2:User {{name: "{second_username}"}})
#         MERGE (u1)-[:FOLLOWS]->(u2)"""

#     @staticmethod
#     def unfollow_user_command(first_username: str, second_username: str):
#         return f"""MATCH (u1:User {{name: "{first_username}"}})-[r:FOLLOWS]->(u2:User {{name: "{second_username}"}})
#         DELETE r"""

import os

from dotenv import load_dotenv
from neomodel import config

from database.graph.nodes.user import User as UserNode
from schemas.user import User as UserModel

load_dotenv(".environment")


class UserGraphRepository:
    def __init__(self) -> None:
        config.DATABASE_URL = os.getenv("NEO4J_BOLT_URL")

    def get_all_users(self) -> list:
        return UserNode.nodes.all()

    def create_user(self, user_model: UserModel) -> UserNode:
        user = UserNode(username=user_model.username).save()
        return user

    def get_all_following_users(self, username: str) -> list[UserNode]:
        user = UserNode.nodes.first(username=username)
        # following_users_of_user = user.follows.all()
        return user

    def get_all_user_followers(self):
        pass

    def follow_user(self, first_username: str, second_username) -> None:
        first_user = UserNode.nodes.first(username=first_username)
        second_user = UserNode.nodes.first(username=second_username)
        first_user.follows.connect(second_user)

    def unfollow_user(self, first_username: str, second_username):
        first_user = UserNode.nodes.first(username=first_username)
        second_user = UserNode.nodes.first(username=second_username)
        first_user.follows.disconnect(second_user)
