from typing import List

import uvicorn
from fastapi import FastAPI, HTTPException

from app.schemas.user import User
from domain.errors.exceptions import UserAlreadyExists, UserNotFound
from domain.entities.user_entity import UserEntity
from data.repositories.user_repository_implementation import UserRepository
from infra.databases.neo4j.neo4j_database import Neo4JDatabase
from infra.databases.postgresql.postgresql_database import PostgreSQLDatabase

app = FastAPI()
postgresql_database = PostgreSQLDatabase()
neo4j_database = Neo4JDatabase()
user_repository = UserRepository(postgresql_database, neo4j_database)


@app.get("/users")
def get_all_users():
    try:
        users = user_repository.get_all_users()
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@app.post("/users", status_code=201)
def create_user(user: User):
    try:
        user_repository.create_user(
            UserEntity(
                user.name,
                user.username,
                user.email,
                user.is_verified,
            )
        )
        return {"detail": "User created successfully", "user": user}
    except UserAlreadyExists as e:
        raise HTTPException(status_code=400, detail=e.message())
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


# TODO
@app.put("/users/{username}")
def update_user(user: User):
    try:
        # TODO
        pass
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


# TODO
@app.delete("/users/{username}")
def delete_user(username: str):
    try:
        # TODO
        pass
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@app.get("/users/{username}/following")
def get_all_following_users(username: str):
    try:
        user = UserEntity(username)
        return user_repository.get_all_following_users(user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@app.get("/users/{username}/followers", response_model=List[User])
def get_all_user_followers(username: str):
    try:
        user = UserEntity(username)
        return user_repository.get_all_user_followers(user)
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
        user_repository.follow_user(first_user, second_user)
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
        user_repository.unfollow_user(first_user, second_user)
        return {"detail": f"{first_username} unfollowed {second_username}"}
    except UserNotFound as e:
        raise HTTPException(status_code=404, detail=e.message())
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
