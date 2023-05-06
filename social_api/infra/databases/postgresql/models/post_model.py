from sqlalchemy import Column, ForeignKey, Integer, LargeBinary, String, Text
from infra.databases.postgresql.config.base_database import Base


class PostModel(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    user_username_fk = Column(String(10), ForeignKey("users.username"))


class VideoPostModel(Base):
    __tablename__ = "videopost"
    post_id_fk = Column(Integer, ForeignKey("post.id"))
    video = Column(LargeBinary, nullable=False)


class TextPostModel(Base):
    __tablename__ = "textpost"
    post_id_fk = Column(Integer, ForeignKey("post.id"))
    text = Column(Text, nullable=False)


class PhotoPostModel(Base):
    __tablename__ = "photopost"
    post_id_fk = Column(Integer, ForeignKey("post.id"))
    photo = Column(LargeBinary, nullable=False)
