__all__ = [
    "Singleton",
]

from threading import Lock


class Singleton:
    __instance = None
    __lock = Lock()

    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            with cls.__lock:
                if cls.__instance is None:
                    cls.__instance = object.__new__(cls)
        return cls.__instance
