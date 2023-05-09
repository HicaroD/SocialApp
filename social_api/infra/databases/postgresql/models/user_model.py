from typing import List


class UserModel:
    def __init__(
        self,
        name: str,
        username: str,
        email: str,
        is_verified: bool,
    ):
        self.name = name
        self.username = username
        self.email = email
        self.is_verified = is_verified

    # TODO
    @staticmethod
    def from_user_list_query(users: List) -> List["UserModel"]:
        pass
