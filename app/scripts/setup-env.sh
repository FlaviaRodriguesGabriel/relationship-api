#!/usr/bin/env bash

virtualenv -p py38 .venv
# shellcheck disable=SC1091
. .venv/bin/activate

pip install --upgrade pip
pip install -r app/requirements-dev.txt

# TODO: add method that merge .env.default into .env
