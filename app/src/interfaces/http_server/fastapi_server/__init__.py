from fastapi import FastAPI

from interfaces.http_server import HttpServer

# TODO: understand how to define FastAPI server controllers
# from .controllers import health_check, index


class FastApiServer(HttpServer):
    fast_api: FastAPI

    def __init__(
        self, app_name: str, environment: str, host: str, port: int, debug: bool = False
    ) -> None:
        HttpServer.__init__(
            self,
            app_name=app_name,
            environment=environment,
            host=host,
            port=port,
            debug=debug,
        )
        # self.fast_api = FastAPI(...)  # TODO: understand how to config FastAPI server

    def run(self) -> None:
        ...
        # self.fast_api...  # TODO: understand how to start FastAPI server
