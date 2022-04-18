#! /usr/bin/env python


def main(clear: bool = False) -> None:
    from app import App

    app = App()
    if not clear:
        app.start_server()
    else:
        app.clear_graph()


if __name__ == "__main__":
    from sys import argv

    # We don't want global variables. No variable is defined in this scope, like `clear`
    main(clear=len(argv) > 1 and argv[1] == "clear")
