from abc import ABC, abstractmethod
from typing import List
from domain.entities.comment import Comment
from domain.entities.post import Post
from domain.entities.user import User


class IUserRepository(ABC):
    @abstractmethod
    def create_user(self, user: User) -> User:
        raise NotImplementedError()

    @abstractmethod
    def update_user(self, user: User) -> User:
        raise NotImplementedError()

    @abstractmethod
    def delete_user(self, user: User) -> User:
        raise NotImplementedError()

    @abstractmethod
    def get_user_by_username(self, username: str) -> User:
        raise NotImplementedError()

    @abstractmethod
    def follow_user(self, first_username: str, second_username: str) -> None:
        raise NotImplementedError()

    @abstractmethod
    def unfollow_user(self, first_username: str, second_username: str) -> None:
        raise NotImplementedError()

    @abstractmethod
    def get_post_from_id(self, post_id: int) -> Post:
        raise NotImplementedError()

    @abstractmethod
    def get_all_user_followers(self, username: str) -> List[User]:
        raise NotImplementedError()

    @abstractmethod
    def get_comments_from_post(self, post_id: int) -> List[Comment]:
        raise NotImplementedError()
