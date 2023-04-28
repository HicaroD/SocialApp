from typing import Generator

import uvicorn
from fastapi import Depends, FastAPI, HTTPException

from app.schemas.user import User
from datasources.user_datasource import UserDatasource
from domain.repositories.user_repository import (
    UserAlreadyExists,
    UserNotFound,
    UserRepository,
)

app = FastAPI()


def get_graph_database() -> Generator[UserRepository, None, None]:
    user_datasource = UserDatasource()
    database = UserRepository(user_datasource)
    yield database


# TODO(refactor): the whole API design could be improved
# Unnecessary code repetition, bad error handling


@app.get("/users", response_model=list[str])
def get_all_registered_users(
    database: UserRepository = Depends(get_graph_database),
):
    try:
        return database.get_all_users()
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@app.post("/users", status_code=201)
def create_user(
    user: User,
    database: UserRepository = Depends(get_graph_database),
):
    try:
        new_user = database.create_user(user)
        return {"detail": "User created successfully", "user": new_user}
    except UserAlreadyExists as e:
        raise HTTPException(status_code=400, detail=f"{e.args[0]}")
    except UserNotFound as e:
        raise HTTPException(status_code=404, detail=f"{e.args[0]}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")


# TODO: update user
# TODO: delete user


@app.get("/users/{username}/following")
def get_all_following_users(
    username: str,
    database: UserRepository = Depends(get_graph_database),
):
    try:
        return database.get_all_following_users(username)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")


@app.get("/users/{username}/followers")
def get_all_user_followers(
    username: str,
    database: UserRepository = Depends(get_graph_database),
):
    try:
        return database.get_all_user_followers(username)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")


@app.post("/users/{first_username}/follow/{second_username}")
def follow(
    first_username: str,
    second_username: str,
    database: UserRepository = Depends(get_graph_database),
):
    try:
        database.follow_user(first_username, second_username)
        return {"detail": f"{first_username} is following {second_username}"}
    except UserNotFound as e:
        raise HTTPException(status_code=404, detail=f"{e.args[0]}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")


@app.post("/users/{first_username}/unfollow/{second_username}")
def unfollow(
    first_username: str,
    second_username: str,
    database: UserRepository = Depends(get_graph_database),
):
    try:
        database.unfollow_user(first_username, second_username)
        return {"detail": f"{first_username} unfollowed {second_username}"}
    except UserNotFound as e:
        raise HTTPException(status_code=404, detail=f"{e.args[0]}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
