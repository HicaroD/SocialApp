from datetime import datetime

from pydantic import BaseModel


class User(BaseModel):
    name: str
    username: str
    birthdate: datetime
    description: str | None
    profile_picture: str | None
