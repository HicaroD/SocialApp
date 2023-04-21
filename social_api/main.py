from fastapi import FastAPI
from models.user import User

app = FastAPI()

@app.get("/users")
def get_all_registered_users():
    # TODO: query database to get all registered users
    pass

@app.post("/users")
def create_user(user: User):
    # TODO: add new user to Neo4J database
    pass

@app.get("/users/{username}/followers")
def get_all_followers_of_user(username: str):
    # TODO: query database to get all users that user with username follows
    pass

@app.post("/users/{first_username}/follow/{second_username}")
def follow(first_username: str, second_username: str):
    # TODO: query database to build a relationship between first username and second username
    pass

@app.post("/users/{first_username}/unfollow/{second_username}")
def unfollow(first_username: str, second_username: str):
    # TODO: query database to remove (if exists) a relationship between first username and 
    # second username
    pass