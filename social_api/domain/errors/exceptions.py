class UserNotFound(Exception):
    def __init__(self, message: str) -> None:
        self._message = message
        super().__init__(message)

    @property
    def message(self):
        return self.args[0]


class UserAlreadyExists(Exception):
    def __init__(self, message: str) -> None:
        self._message = message
        super().__init__(message)

    def message(self):
        return self.args[0]
