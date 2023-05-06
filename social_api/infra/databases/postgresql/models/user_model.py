from sqlalchemy import Boolean, Column, String
from infra.databases.postgresql.config.base_database import Base


class UserModel(Base):
    __tablename__ = "users"

    name = Column(String(50), nullable=False)
    username = Column(String(10), primary_key=True)
    email = Column(String(30), nullable=False)
    is_verified = Column(Boolean, nullable=False)
