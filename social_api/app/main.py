from typing import List

import uvicorn
from fastapi import FastAPI, HTTPException

from app.schemas.user import User
from domain.errors.exceptions import UserAlreadyExists, UserNotFound
from domain.entities.user_entity import UserEntity
from domain.repositories.user_repository_interface import UserRepository

app = FastAPI()


@app.get("/users", response_model=List[str])
def get_all_registered_users():
    try:
        return database.get_all_users()
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@app.post("/users", status_code=201)
def create_user(user: UserEntity):
    try:
        new_user = database.create_user(UserEntity(user.username))
        return {"detail": "User created successfully", "user": new_user}
    except UserAlreadyExists as e:
        raise HTTPException(status_code=400, detail=e.message())
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


# TODO: update user
# TODO: delete user


@app.get("/users/{username}/following")
def get_all_following_users(username: str):
    try:
        user = UserEntity(username)
        return database.get_all_following_users(user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@app.get("/users/{username}/followers", response_model=List[UserEntity])
def get_all_user_followers(username: str):
    try:
        user = UserEntity(username)
        return database.get_all_user_followers(user)
    except UserNotFound as e:
        raise HTTPException(status_code=404, detail=e.message())
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@app.post("/users/{first_username}/follow/{second_username}")
def follow(
    first_username: str,
    second_username: str,
):
    try:
        first_user = UserEntity(first_username)
        second_user = UserEntity(second_username)
        database.follow_user(first_user, second_user)
        return {"detail": f"{first_username} is following {second_username}"}
    except UserNotFound as e:
        raise HTTPException(status_code=404, detail=e.message())
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@app.post("/users/{first_username}/unfollow/{second_username}")
def unfollow(
    first_username: str,
    second_username: str,
):
    try:
        first_user = UserEntity(first_username)
        second_user = UserEntity(second_username)
        database.unfollow_user(first_user, second_user)
        return {"detail": f"{first_username} unfollowed {second_username}"}
    except UserNotFound as e:
        raise HTTPException(status_code=404, detail=e.message())
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
