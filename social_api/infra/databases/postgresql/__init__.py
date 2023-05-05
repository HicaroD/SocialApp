from infra.databases.postgresql.config.base_database import Base
from infra.databases.postgresql.config.database_connection import DatabaseConnection

database_connection = DatabaseConnection()
Base.metadata.create_all(database_connection.get_engine())
