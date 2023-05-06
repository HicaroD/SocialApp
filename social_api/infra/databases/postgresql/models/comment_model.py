from sqlalchemy import Column, Integer, Text
from infra.databases.postgresql.config.base_database import Base


class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True)
    text = Column(Text, nullable=False)
