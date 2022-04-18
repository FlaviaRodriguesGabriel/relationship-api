from abc import ABC, abstractmethod


class HttpServer(ABC):
    app_name: str
    environment: str
    host: str
    port: int
    debug: bool

    def __init__(
        self,
        app_name: str,
        environment: str,
        host: str,
        port: int,
        debug: bool = False,
    ) -> None:
        self.app_name = app_name
        self.debug = debug
        self.environment = environment
        self.host = host
        self.port = port

    @abstractmethod
    def run(self) -> None:
        ...
