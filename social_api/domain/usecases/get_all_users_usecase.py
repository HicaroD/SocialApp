from domain.repositories.user_repository_interface import IUserRepository


class GetAllUsersUsecase:
    def __init__(self, user_repository: IUserRepository) -> None:
        pass