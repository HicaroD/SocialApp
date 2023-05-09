from typing import List
import psycopg2


class DatabaseConnection:
    def __init__(self) -> None:
        self._user = "postgres"
        self._password = "example"
        self._host = "postgresql_container"
        self._port = "5432"
        self._database = "postgres"

        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = self._get_connection()
        self.cursor = self._get_cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.connection.close()

    def execute_query(self, query: str):
        self.cursor.execute(query)
    
    def fetch_all_results(self) -> List:
        return self.cursor.fetchall()

    def _get_connection(self):
        connection = psycopg2.connect(
            host=self._host,
            port=self._port,
            dbname=self._database,
            user=self._user,
            password=self._password,
        )
        connection.autocommit = True
        return connection

    def _get_cursor(self):
        connection = self._get_connection()
        return connection.cursor()
