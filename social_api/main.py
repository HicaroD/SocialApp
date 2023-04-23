import os
from typing import Generator

from dotenv import dotenv_values
from fastapi import Depends, FastAPI, HTTPException

from database.connection import SocialAppDatabase
from models.user import User

CONFIG = dotenv_values(".environment")

app = FastAPI()


def get_graph_database() -> Generator[SocialAppDatabase, None, None]:
    try:
        database = SocialAppDatabase(
            CONFIG["NEO4J_URL"],
            CONFIG["NEO4J_USERNAME"],
            CONFIG["NEO4J_PASSWORD"],
        )
        yield database
    finally:
        database.close()


# TODO(refactor): the whole API design could be improved
# Unnecessary code repetition


@app.get("/users")
def get_all_registered_users(
    database: SocialAppDatabase = Depends(get_graph_database),
):
    try:
        return database.get_all_users()
    except Exception:
        raise HTTPException(status_code=500, detail="An error ocurred")


@app.post("/users", status_code=201)
def create_user(
    user: User,
    database: SocialAppDatabase = Depends(get_graph_database),
):
    try:
        database.create_user(user)
        return {"detail": "User created successfully"}
    except Exception:
        raise HTTPException(status_code=500, detail="An error ocurred")


@app.get("/users/{username}/following")
def get_all_following_users(
    username: str,
    database: SocialAppDatabase = Depends(get_graph_database),
):
    try:
        return database.get_all_following_users(username)
    except Exception:
        raise HTTPException(status_code=500, detail="An error ocurred")


@app.get("/users/{username}/followers")
def get_all_user_followers(
    username: str,
    database: SocialAppDatabase = Depends(get_graph_database),
):
    try:
        return database.get_all_users_followers(username)
    except Exception:
        raise HTTPException(status_code=500, detail="An error ocurred")


@app.post("/users/{first_username}/follow/{second_username}")
def follow(
    first_username: str,
    second_username: str,
    database: SocialAppDatabase = Depends(get_graph_database),
):
    try:
        database.follow_user(first_username, second_username)
        return {"detail": f"{first_username} is following {second_username}"}
    except Exception:
        raise HTTPException(status_code=500, detail="An error ocurred")


@app.post("/users/{first_username}/unfollow/{second_username}")
def unfollow(
    first_username: str,
    second_username: str,
    database: SocialAppDatabase = Depends(get_graph_database),
):
    try:
        database.unfollow_user(first_username, second_username)
        return {"detail": f"{first_username} unfollowed {second_username}"}
    except Exception:
        raise HTTPException(status_code=500, detail="An error ocurred")
