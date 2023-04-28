from datasources.errors.graph import UserAlreadyExists, UserNotFound
from datasources.user_datasource import UserDatasource
from domain.entities.user import UserEntity


# TODO: implement methods and handle errors that can come from UserDatasource
class UserRepository:
    def __init__(
        self,
        user_datasource: UserDatasource,
    ) -> None:
        self.user_datasource = user_datasource

    def get_all_users(self) -> list[str]:
        return self.user_datasource.get_all_users()

    def create_user(self, user_entity: UserEntity) -> UserEntity:
        # TODO
        pass

    def get_all_following_users(self, user_entity: UserEntity) -> list[str]:
        # TODO
        pass

    def get_all_user_followers(self, username: str) -> list[str]:
        # TODO
        pass

    def follow_user(self, first_user: UserEntity, second_user: UserEntity) -> None:
        # TODO
        pass

    def unfollow_user(self, first_user: UserEntity, second_user: UserEntity) -> None:
        # TODO
        pass
