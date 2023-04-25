from neo4j import GraphDatabase
from models.user import User
from database.neo4j.commands import CypherCommands


class SocialAppDatabase:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def get_all_users(self) -> list:
        return self._query_read(CypherCommands.get_all_users_command())

    def create_user(self, user: User) -> None:
        return self._query_write(CypherCommands.get_create_user_command(user))

    def get_all_following_users(self, username: str) -> None:
        return self._query_read(CypherCommands.get_all_following_users(username))

    def get_all_users_followers(self, username: str) -> list:
        return self._query_read(
            CypherCommands.get_all_users_followers_command(username)
        )

    def follow_user(self, first_username: str, second_username: str) -> None:
        return self._query_write(
            CypherCommands.follow_user_command(first_username, second_username)
        )

    def unfollow_user(self, first_username: str, second_username: str) -> None:
        return self._query_write(
            CypherCommands.unfollow_user_command(first_username, second_username)
        )

    def _query_read(self, command: str) -> list:
        with self.driver.session() as session:
            result = session.execute_read(self._do_cypher_tx, command)
        return result

    def _query_write(self, command: str) -> list:
        with self.driver.session() as session:
            result = session.execute_write(self._do_cypher_tx, command)
        return result

    def _do_cypher_tx(self, tx, cypher) -> list:
        result = tx.run(cypher)
        values = [record.values() for record in result]
        return values

    def close(self):
        self.driver.close()


def main() -> None:
    database = SocialAppDatabase("bolt://127.0.0.1:7687", "neo4j", "password")
    database.create_user(
        User(
            name="hicaro",
            description="My name is Hícaro and I like Counter Strike",
            age=19,
        )
    )
    database.create_user(
        User(
            name="alice",
            description="My name is Alice and I like Valorant",
            age=19,
        )
    )
    database.follow_user("alice", "hicaro")
    database.follow_user("hicaro", "alice")

    print(database.get_all_users())
    database.close()


if __name__ == "__main__":
    main()
