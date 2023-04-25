from pydantic import BaseModel


class User(BaseModel):
    name: str
    username: str
    age: int
    description: str | None
    profile_picture: str | None
