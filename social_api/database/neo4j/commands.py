from models.user import User

# TODO(REFACTOR): lines are too big!
# I'll be using a OGM for Neo4J in order to simplify all queries


class CypherCommands:
    @staticmethod
    def get_all_users_command():
        return "MATCH (user: User) RETURN user"

    @staticmethod
    def get_create_user_command(user: User):
        name = user.name
        username = user.username
        age = user.age
        description = "" if user.description is None else user.description
        profile_picture = "" if user.profile_picture is None else user.profile_picture

        return f"""MERGE (user: User {{username: "{username}", name: "{name}", "age: "{age}", description: "{description}", profile_picture: "{profile_picture}"}})"""

    @staticmethod
    def get_all_following_users(username: str):
        return f"""MATCH (u:User {{name: "{username}"}})-[:FOLLOWS]->(following) 
        RETURN following"""

    @staticmethod
    def get_all_users_followers_command(username: str):
        return f"""MATCH (u:User {{name: "{username}"}})<-[:FOLLOWS]-(follower)
        RETURN follower"""

    @staticmethod
    def follow_user_command(first_username: str, second_username: str):
        return f"""MATCH (u1:User {{name: "{first_username}"}}), (u2:User {{name: "{second_username}"}})
        MERGE (u1)-[:FOLLOWS]->(u2)"""

    @staticmethod
    def unfollow_user_command(first_username: str, second_username: str):
        return f"""MATCH (u1:User {{name: "{first_username}"}})-[r:FOLLOWS]->(u2:User {{name: "{second_username}"}}) 
        DELETE r"""
