from models.user import User


class CypherCommands:
    @staticmethod
    def get_all_users_command():
        return "MATCH (user: User) RETURN user"

    @staticmethod
    def get_create_user_command(user: User):
        name = user.name
        age = user.age
        description = user.description

        return f"""MERGE (user: User {{name: "{name}", age: "{age}", description: "{description}"}})"""

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
