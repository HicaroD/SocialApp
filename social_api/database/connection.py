from neo4j import GraphDatabase
from models.user import User
from database.commands import CypherCommands


class SocialAppDatabase:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def get_all_users(self):
        return self._query_read(CypherCommands.get_all_users_command())

    def create_user(self, user: User):
        return self._query_write(CypherCommands.get_create_user_command(user))

    def get_all_following_users(self, username: str):
        return self._query_read(CypherCommands.get_all_following_users(username))

    def get_all_users_followers(self, username: str):
        return self._query_read(
            CypherCommands.get_all_users_followers_command(username)
        )

    def follow_user(self, first_username: str, second_username: str):
        return self._query_write(
            CypherCommands.follow_user_command(first_username, second_username)
        )

    def unfollow_user(self, first_username: str, second_username: str):
        return self._query_write(
            CypherCommands.unfollow_user_command(first_username, second_username)
        )

    def _query_read(self, command: str):
        with self.driver.session() as session:
            result = session.execute_read(self._do_cypher_tx, command)
        return result

    def _query_write(self, command: str):
        with self.driver.session() as session:
            result = session.execute_write(self._do_cypher_tx, command)
        return result

    def _do_cypher_tx(self, tx, cypher):
        result = tx.run(cypher)
        values = [record.values() for record in result]
        return values

    def close(self):
        self.driver.close()


if __name__ == "__main__":
    database = SocialAppDatabase("bolt://127.0.0.1:7687", "neo4j", "password")
    print(database.get_all_users())
    database.close()
