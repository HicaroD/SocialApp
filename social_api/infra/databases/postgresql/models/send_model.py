from sqlalchemy import Column, Integer, ForeignKey, String
from infra.databases.postgresql.config.base_database import Base


class Send(Base):
    __tablename__ = "send"

    post_id_fk = Column(Integer, ForeignKey("post.id"), primary_key=True)
    comment_id_fk = Column(Integer, ForeignKey("comment.id"), primary_key=True)
    user_username_fk = Column(String(10), ForeignKey("users.username"), nullable=False)
