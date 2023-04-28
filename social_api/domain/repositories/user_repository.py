from datasources.user_datasource import UserDatasource
from domain.entities.user import UserEntity


class UserRepository:
    def __init__(
        self,
        user_datasource: UserDatasource,
    ) -> None:
        self.user_datasource = user_datasource

    def get_all_users(self) -> list[str]:
        return self.user_datasource.get_all_users()

    def create_user(self, user_entity: UserEntity) -> UserEntity:
        new_user = self.user_datasource.create_user(user_entity)
        return UserEntity(new_user.username)

    def get_all_following_users(self, user_entity: UserEntity) -> list[str]:
        return self.user_datasource.get_all_following_users(user_entity)

    def get_all_user_followers(self, user_entity: UserEntity) -> list[str]:
        return self.user_datasource.get_all_following_users(user_entity)

    def follow_user(self, first_user: UserEntity, second_user: UserEntity) -> None:
        self.user_datasource.follow_user(first_user, second_user)

    def unfollow_user(self, first_user: UserEntity, second_user: UserEntity) -> None:
        self.user_datasource.unfollow_user(first_user, second_user)
