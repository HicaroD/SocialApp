from neo4j import GraphDatabase

# TODO: build a context manager with this class for interacting with the DB
class SocialAppDatabase:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
    
    def print_greeting(self, message):
        with self.driver.session() as session:
            greeting = session.execute_write(self._create_and_return_greeting, message)
            print(greeting)

    @staticmethod
    def _create_and_return_greeting(tx, message):
        result = tx.run("CREATE (a:Greeting) "
                        "SET a.message = $message "
                        "RETURN a.message + ', from node ' + id(a)", message=message)
        return result.single()[0]

    def close(self):
        self.driver.close()


if __name__ == "__main__":
    greeter = SocialAppDatabase("bolt://127.0.0.1:7687", "neo4j", "password")
    greeter.print_greeting("hello, world")
    greeter.close()