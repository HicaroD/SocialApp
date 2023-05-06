import time
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

from infra.databases.postgresql.config.base_database import Base


class DatabaseConnection:
    def __init__(self) -> None:
        self._user = "postgres"
        self._password = "example"
        self._host = "localhost"
        self._port = "5432"
        self._database = "postgres"

    def get_engine(self):
        engine = None
        while not engine:
            try:
                engine = create_engine(self._build_connection_string())
                print(engine)
            except OperationalError:
                print("Database not ready yet, waiting...")
                time.sleep(1)
            except Exception as e:
                print(f"Error: {e}")
                raise

        print("PostgreSQL is connected")
        Base.metadata.create_all(engine)
        return engine

    def _build_connection_string(self):
        return f"postgresql+psycopg2://{self._user}:{self._password}@{self._host}:{self._port}/{self._database}"
