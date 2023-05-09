import time
import psycopg2


class DatabaseConnection:
    def __init__(self) -> None:
        self._user = "postgres"
        self._password = "example"
        self._host = "localhost"
        self._port = "5000"
        self._database = "postgres"

    def get_cursor(self):
        # TODO: connect to database and create cursor
        pass
