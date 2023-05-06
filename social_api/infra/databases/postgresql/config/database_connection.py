from sqlalchemy import create_engine


class DatabaseConnection:
    def __init__(self) -> None:
        # TODO: hide these configurations data?
        self._user = "postgres"
        self._password = "example"
        self._host = "localhost"
        self._port = "5432"
        self._database = "socialapp"

        self._connection_string = self._build_connection_string()

    def get_engine(self):
        return create_engine(self._connection_string)

    def _build_connection_string(self):
        return f"postgresql+psycopg2://{self._user}:{self._password}@{self._host}:{self._port}/{self._database}"
