from abc import ABC, abstractmethod
from typing import List
from domain.entities.comment_entity import CommentEntity
from domain.entities.post_entity import PostEntity
from domain.entities.user_entity import UserEntity


class IUserRepository(ABC):
    @abstractmethod
    def get_all_users(self) -> UserEntity:
        raise NotImplementedError()

    @abstractmethod
    def create_user(self, user: UserEntity) -> UserEntity:
        raise NotImplementedError()

    @abstractmethod
    def update_user(self, user: UserEntity) -> UserEntity:
        raise NotImplementedError()

    @abstractmethod
    def delete_user(self, user: UserEntity) -> UserEntity:
        raise NotImplementedError()

    @abstractmethod
    def get_user_by_username(self, username: str) -> UserEntity:
        raise NotImplementedError()

    @abstractmethod
    def follow_user(self, first_username: str, second_username: str) -> None:
        raise NotImplementedError()

    @abstractmethod
    def unfollow_user(self, first_username: str, second_username: str) -> None:
        raise NotImplementedError()

    @abstractmethod
    def get_post_from_id(self, post_id: int) -> PostEntity:
        raise NotImplementedError()

    @abstractmethod
    def get_all_user_followers(self, username: str) -> List[UserEntity]:
        raise NotImplementedError()

    @abstractmethod
    def get_comments_from_post(self, post_id: int) -> List[CommentEntity]:
        raise NotImplementedError()
