from typing import Optional

import uvicorn

from .settings.components import config


class Django:
    host: str
    port: int
    reload: bool
    workers: Optional[int]

    def __init__(
        self,
        *args,
        host: str = "127.0.0.1",
        port: int = config("HTTP_PORT", default=8081, cast=int),
        reload: bool = config("AUTO_RELOAD", default=False, cast=bool),
        workers: Optional[int] = config("HTTP_WORKERS", default=0, cast=int),
        **kwargs,
    ) -> None:
        self.host = host
        self.port = port
        self.reload = reload
        self.workers = workers or None
        super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"host={self.host}, "
            f"port={self.port}, "
            f"reload={self.reload}, "
            f"workers={self.workers}, "
            ")"
        )

    def run(self):
        uvicorn.run(
            app="inputs.http_server.asgi:application",
            host=self.host,
            port=self.port,
            log_level="info",
            reload=self.reload,
            workers=self.workers,
        )
