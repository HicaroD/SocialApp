from pydantic import BaseModel


class TextPost(BaseModel):
    text: str


class VideoPost(BaseModel):
    video: str


class PhotoPost(BaseModel):
    photo: str
