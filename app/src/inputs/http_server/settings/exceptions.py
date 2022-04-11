from typing import Optional


class UnkownEnvironment(Exception):
    message = "The ENVIRONMENT variable setup does not have a correspondent file"

    def __init__(self, message: Optional[str] = None, *args) -> None:
        self.message = message or self.message

        super().__init__(self.message, *args)
