from fastapi import FastAPI, HTTPException

from database.connection import SocialAppDatabase
from models.user import User

app = FastAPI()
database = SocialAppDatabase("bolt://127.0.0.1:7687", "neo4j", "password")

# TODO(refactor): the whole API design could be better and simpler.


@app.get("/users")
def get_all_registered_users():
    try:
        return database.get_all_users()
    except Exception:
        raise HTTPException(status_code=500, detail="An error ocurred")


@app.post("/users", status_code=201)
def create_user(user: User):
    try:
        database.create_user(user)
        return {"detail": "User created successfully"}
    except Exception:
        raise HTTPException(status_code=500, detail="An error ocurred")


@app.get("/users/{username}/following")
def get_all_following_users(username: str):
    try:
        return database.get_all_following_users(username)
    except Exception:
        raise HTTPException(status_code=500, detail="An error ocurred")


@app.get("/users/{username}/followers")
def get_all_user_followers(username: str):
    try:
        return database.get_all_users_followers(username)
    except Exception:
        raise HTTPException(status_code=500, detail="An error ocurred")


@app.post("/users/{first_username}/follow/{second_username}")
def follow(first_username: str, second_username: str):
    try:
        database.follow_user(first_username, second_username)
        return {"detail": f"{first_username} is following {second_username}"}
    except Exception:
        raise HTTPException(status_code=500, detail="An error ocurred")


@app.post("/users/{first_username}/unfollow/{second_username}")
def unfollow(first_username: str, second_username: str):
    try:
        database.unfollow_user(first_username, second_username)
        return {"detail": f"{first_username} unfollowed {second_username}"}
    except Exception:
        raise HTTPException(status_code=500, detail="An error ocurred")
