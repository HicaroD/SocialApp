from typing import Generator

import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from database.errors.graph import UserAlreadyExists, UserNotFound

from database.graph.repository import UserGraphRepository
from schemas.user import User

app = FastAPI()


def get_graph_database() -> Generator[UserGraphRepository, None, None]:
    database = UserGraphRepository()
    yield database


# TODO(refactor): the whole API design could be improved
# Unnecessary code repetition, bad error handling


@app.get("/users", response_model=list[str])
def get_all_registered_users(
    database: UserGraphRepository = Depends(get_graph_database),
):
    try:
        return database.get_all_users()
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@app.post("/users", status_code=201)
def create_user(
    user: User,
    database: UserGraphRepository = Depends(get_graph_database),
):
    try:
        new_user = database.create_user(user)
        return {"detail": "User created successfully", "user": new_user}
    except UserAlreadyExists as e:
        raise HTTPException(status_code=400, detail=f"{e.args[0]}")
    except UserNotFound as e:
        raise HTTPException(status_code=404, detail=f"{e.args[0]}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e.message}")


# TODO: update user
# TODO: delete user


@app.get("/users/{username}/following")
def get_all_following_users(
    username: str,
    database: UserGraphRepository = Depends(get_graph_database),
):
    try:
        return database.get_all_following_users(username)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")


@app.get("/users/{username}/followers")
def get_all_user_followers(
    username: str,
    database: UserGraphRepository = Depends(get_graph_database),
):
    try:
        return database.get_all_user_followers(username)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e.message}")


@app.post("/users/{first_username}/follow/{second_username}")
def follow(
    first_username: str,
    second_username: str,
    database: UserGraphRepository = Depends(get_graph_database),
):
    try:
        database.follow_user(first_username, second_username)
        return {"detail": f"{first_username} is following {second_username}"}
    except UserNotFound as e:
        raise HTTPException(status_code=404, detail=f"{e.args[0]}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e.message}")


@app.post("/users/{first_username}/unfollow/{second_username}")
def unfollow(
    first_username: str,
    second_username: str,
    database: UserGraphRepository = Depends(get_graph_database),
):
    try:
        database.unfollow_user(first_username, second_username)
        return {"detail": f"{first_username} unfollowed {second_username}"}
    except UserNotFound as e:
        raise HTTPException(status_code=404, detail=f"{e.args[0]}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e.message}")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
