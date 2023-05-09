from pydantic import BaseModel


class Post(BaseModel):
    pass


class TextPostEntity(Post):
    text: str


class VideoPostEntity(Post):
    video: str


class PhotoPost(Post):
    photo: str
