from flask import Flask

from interfaces.http_server import HttpServer

from .controllers import health_check, index


class FlaskServer(HttpServer):
    flask: Flask

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
        self.flask = Flask(app_name)
        self.flask.env = environment
        self.register_controllers()

    def register_controllers(self) -> None:
        # TODO: find a way to auto-register all blueprints from path: ./controllers
        self.flask.register_blueprint(index)
        self.flask.register_blueprint(health_check)

    def run(self) -> None:
        self.flask.run(
            debug=self.debug,
            host=self.host,
            load_dotenv=False,
            port=self.port,
            threaded=True,
        )
