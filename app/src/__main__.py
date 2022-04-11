#! /usr/bin/env python

from sys import argv

from app import App


# from loguru import logger
# @logger.catch
def main(clear: bool = False) -> App:
    app = App(clear_on_startup=clear)
    app.start_server()
    return app


if __name__ == "__main__":
    if len(argv) > 1 and argv[1] == "clear":
        clear = True
    else:
        clear = False

    app = main(clear=clear)
