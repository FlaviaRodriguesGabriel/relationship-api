#!/usr/bin/env python

from sys import argv

from loguru import logger

from app import App


@logger.catch
def main(clear=False):
    app = App(clear_on_startup=clear)
    app.start_server()
    return app


if __name__ == "__main__":
    if len(argv) > 1 and argv[1] == "clear":
        clear = True
    else:
        clear = False

    app = main(clear=clear)
