from pydantic import BaseModel


class Post(BaseModel):
    pass


class TextPost(Post):
    text: str


class VideoPost(Post):
    video: str


class PhotoPost(Post):
    photo: str
