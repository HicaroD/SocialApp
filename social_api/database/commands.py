from models.user import User


class CypherCommands:
    @staticmethod
    def get_all_users_command():
        return "MATCH (user: User) RETURN user"

    @staticmethod
    def get_create_user_command(user: User):
        username = user.username
        age = user.age
        description = user.description

        return f'CREATE (user: User {{name: "{username}", age: "{age}", description: "{description}"}})'

    @staticmethod
    def get_all_users_followers_command(username: str):
        # TODO
        pass

    @staticmethod
    def follow_user_command(first_username: str, second_username: str):
        # TODO
        pass

    @staticmethod
    def unfollow_user_command(first_username: str, second_username: str):
        # TODO
        return
