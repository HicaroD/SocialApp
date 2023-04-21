from pydantic import BaseModel

class User(BaseModel):
    username: str
    age: int
    description: str