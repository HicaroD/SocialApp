from typing import List

import uvicorn
from fastapi import FastAPI, HTTPException
from app.schemas.comment import Comment
from app.schemas.post import PhotoPost, TextPost, VideoPost

from app.schemas.user import User
from domain.entities.comment_entity import CommentEntity
from domain.entities.post_entity import (
    PhotoPostEntity,
    TextPostEntity,
    VideoPostEntity,
)
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
        return {"users": users}
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@app.get("/users/{username}")
def get_user(username: str):
    try:
        user = user_repository.get_user_by_username(username)
        return {"user": user}
    except UserNotFound as e:
        raise HTTPException(status_code=404, detail=e.message)
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
        raise HTTPException(status_code=400, detail=e.message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@app.put("/users/{username}")
def update_user(username: str, user: User):
    try:
        user_repository.update_user(
            username,
            UserEntity(
                user.name,
                user.username,
                user.email,
                user.is_verified,
            ),
        )
        return {
            "detail": "User was successfuly updated",
            "user": user,
        }
    except UserNotFound as e:
        raise HTTPException(status_code=404, detail=e.message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@app.delete("/users/{username}")
def delete_user(username: str):
    try:
        user_repository.delete_user(username)
        return {"detail": f"User with username '{username} was deleted successfuly'"}
    except UserNotFound as e:
        raise HTTPException(status_code=404, detail=e.message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@app.get("/users/{username}/following")
def get_all_following_users(username: str):
    try:
        following_users = user_repository.get_all_following_users(username)
        return {"users": following_users}
    except UserNotFound as e:
        raise HTTPException(status_code=404, detail=e.message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@app.get("/users/{username}/followers", response_model=List[User])
def get_all_user_followers(username: str):
    try:
        followers = user_repository.get_all_user_followers(username)
        return {"users": followers}
    except UserNotFound as e:
        raise HTTPException(status_code=404, detail=e.message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@app.post("/users/{first_username}/follow/{second_username}")
def follow(
    first_username: str,
    second_username: str,
):
    try:
        user_repository.follow_user(first_username, second_username)
        return {"detail": f"{first_username} is following {second_username}"}
    except UserNotFound as e:
        raise HTTPException(status_code=404, detail=e.message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@app.post("/users/{first_username}/unfollow/{second_username}")
def unfollow(
    first_username: str,
    second_username: str,
):
    try:
        user_repository.unfollow_user(first_username, second_username)
        return {"detail": f"{first_username} unfollowed {second_username}"}
    except UserNotFound as e:
        raise HTTPException(status_code=404, detail=e.message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@app.post("/users/{username}/post_photo/")
def post_photo(
    username: str,
    photo: PhotoPost,
):
    try:
        user_repository.post_photo(username, PhotoPostEntity(photo.photo))
        return {"detail": f"Photo was posted by {username}"}
    except UserNotFound as e:
        raise HTTPException(status_code=404, detail=e.message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@app.post("/users/{username}/post_video/")
def post_video(
    username: str,
    video: VideoPost,
):
    try:
        user_repository.post_video(username, VideoPostEntity(video.video))
        return {"detail": f"Video was posted by {username}"}
    except UserNotFound as e:
        raise HTTPException(status_code=404, detail=e.message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@app.post("/users/{username}/post_text/")
def post_text(
    username: str,
    text: TextPost,
):
    try:
        user_repository.post_text(username, TextPostEntity(text.text))
        return {"detail": f"Text was posted by {username}"}
    except UserNotFound as e:
        raise HTTPException(status_code=404, detail=e.message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@app.get("/users/{username}/posts")
def get_all_user_post_ids(username: str):
    try:
        posts = user_repository.get_all_posts_from_user(username)
        return posts
    except UserNotFound as e:
        raise HTTPException(status_code=404, detail=e.message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@app.delete("/post/{post_id}")
def delete_post(post_id: int):
    try:
        user_repository.delete_post(post_id)
        return {"detail": f"Post was deleted"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@app.post("/users/{username}/posts/{post_id}/comment")
def comment_in_post(username: str, post_id: int, comment: Comment):
    try:
        user_repository.comment_in_post(username, post_id, CommentEntity(comment.text))
        return {"detail": f"{username} commented in the post with id {post_id}"}
    except UserNotFound as e:
        raise HTTPException(status_code=404, detail=e.message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@app.get("/posts/{post_id}/comment")
def get_all_comments_from_post(post_id: int):
    try:
        comments = user_repository.get_comments_from_post(post_id)
        return comments
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
