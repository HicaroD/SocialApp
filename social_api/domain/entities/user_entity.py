class UserEntity:
    def __init__(
        self,
        name: str,
        username: str,
        email: str,
        is_verified: bool = False,
    ) -> None:
        self.name = name
        self.username = username
        self.email = email
        self.is_verified = is_verified
